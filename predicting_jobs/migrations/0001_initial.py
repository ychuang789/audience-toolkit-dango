# Generated by Django 3.1.13 on 2021-11-22 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modeling_jobs', '0001_initial'),
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
                ('job_status', models.CharField(choices=[('created', '已建立'), ('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='任務狀態')),
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
                ('port', models.IntegerField(default=3306, verbose_name='資料庫連接埠')),
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
                ('begin_post_time', models.DateField(verbose_name='起始發文時間')),
                ('end_post_time', models.DateField(verbose_name='結束發文時間')),
                ('min_content_length', models.IntegerField(default=10, verbose_name='最小文章長度')),
                ('max_content_length', models.IntegerField(default=2000, verbose_name='最大文章長度')),
                ('job_status', models.CharField(choices=[('created', '已建立'), ('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='任務狀態')),
                ('task_id', models.CharField(default=None, max_length=255, null=True, verbose_name='排程任務id')),
                ('error_message', models.TextField(null=True, verbose_name='錯誤訊息')),
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
                ('label_name', models.CharField(max_length=200, verbose_name='標籤名稱')),
                ('data_id', models.CharField(max_length=200, verbose_name='預測文章ID')),
                ('source_author', models.CharField(default='UNK', max_length=200, verbose_name='作者')),
                ('applied_feature', models.CharField(choices=[('id', '文章id'), ('s_id', '來源'), ('s_area_id', '來源網站'), ('title', '標題'), ('author', '作者'), ('content', '內文'), ('post_time', '發文時間')], default='content', max_length=50, verbose_name='特徵欄位')),
                ('applied_meta', models.JSONField(null=True, verbose_name='預測細節')),
                ('applied_content', models.TextField(null=True, verbose_name='命中內容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('applied_model', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='modeling_jobs.modelingjob', verbose_name='命中模型')),
                ('predicting_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting_jobs.predictingtarget', verbose_name='預測資料範圍')),
            ],
            options={
                'verbose_name': '預測結果',
                'verbose_name_plural': '預測結果列表',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ApplyingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=0, verbose_name='優先度')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('modeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeling_jobs.modelingjob', verbose_name='應用模型任務')),
                ('predicting_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting_jobs.predictingjob', verbose_name='族群貼標任務')),
            ],
            options={
                'verbose_name': '應用模型',
                'verbose_name_plural': '應用模型列表',
                'ordering': ('priority', 'created_at'),
                'unique_together': {('predicting_job', 'modeling_job')},
            },
        ),
    ]
