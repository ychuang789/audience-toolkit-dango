# Generated by Django 3.1.8 on 2021-04-13 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modeling_jobs', '0001_initial'),
        ('labeling_jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictingJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='預測工作名稱')),
                ('description', models.TextField(verbose_name='定義與說明')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最後更改')),
                ('job_status', models.CharField(choices=[('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='任務狀態')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='建立者')),
            ],
            options={
                'verbose_name': '預測任務',
                'verbose_name_plural': '預測任務列表',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='來源名稱')),
                ('description', models.TextField(verbose_name='定義與說明')),
                ('host', models.CharField(default='localhost', max_length=200, null=True, verbose_name='資料庫位置')),
                ('username', models.CharField(default='root', max_length=100, null=True, verbose_name='資料庫使用者')),
                ('password', models.CharField(default='password', max_length=100, null=True, verbose_name='資料庫密碼')),
                ('port', models.CharField(default='3306', max_length=6, verbose_name='資料庫連接埠')),
                ('schema', models.CharField(default='wh_bbs_01', max_length=100, null=True, verbose_name='資料庫名稱')),
                ('tablename', models.CharField(default='ts_page_content', max_length=100, verbose_name='資料表名稱')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最後更改')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='建立者')),
            ],
            options={
                'verbose_name': '資料源',
                'verbose_name_plural': '資料源列表',
            },
        ),
        migrations.CreateModel(
            name='PredictingTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='預測目標名稱')),
                ('description', models.TextField(verbose_name='定義與說明')),
                ('begin_post_time', models.DateTimeField(verbose_name='起始發文時間')),
                ('end_post_time', models.DateTimeField(verbose_name='結束發文時間')),
                ('min_content_length', models.IntegerField(default=10, verbose_name='最小文章長度')),
                ('max_content_length', models.IntegerField(default=2000, verbose_name='最大文章長度')),
                ('job_status', models.CharField(choices=[('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='任務狀態')),
                ('predicting_job', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='predicting_jobs.predictingjob', verbose_name='預測任務')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='predicting_jobs.source', verbose_name='預測資料源')),
            ],
            options={
                'verbose_name': '預測範圍',
                'verbose_name_plural': '預測範圍列表',
            },
        ),
        migrations.CreateModel(
            name='PredictingResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(verbose_name='預測分數')),
                ('data_id', models.CharField(max_length=200, verbose_name='預測文章ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.label', verbose_name='預測標籤名稱')),
                ('predicting_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting_jobs.predictingtarget', verbose_name='預測資料範圍')),
            ],
            options={
                'verbose_name': '預測結果',
                'verbose_name_plural': '預測結果列表',
            },
        ),
        migrations.CreateModel(
            name='ApplyingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('modeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeling_jobs.modelingjob', verbose_name='應用模型任務')),
                ('predicting_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting_jobs.predictingjob')),
            ],
            options={
                'verbose_name': '應用模型',
                'verbose_name_plural': '應用模型列表',
                'unique_together': {('predicting_job', 'modeling_job')},
            },
        ),
    ]
