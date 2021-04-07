# Generated by Django 3.2 on 2021-04-07 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelingJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='標記工作名稱')),
                ('description', models.TextField(verbose_name='定義與說明')),
                ('is_multi_label', models.BooleanField(default=False, verbose_name='是否屬於多標籤')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最後更改')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '資料標記工作',
                'verbose_name_plural': '資料標記工作列表',
            },
        ),
        migrations.CreateModel(
            name='UploadFileJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload_files', verbose_name='檔案')),
                ('job_status', models.CharField(choices=[('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='任務狀態')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('labeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.labelingjob', verbose_name='所屬任務')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='標籤名稱')),
                ('description', models.TextField(blank=True, verbose_name='標籤定義')),
                ('target_amount', models.IntegerField(default=200, verbose_name='目標數量')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最後更改')),
                ('labeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.labelingjob', verbose_name='所屬任務')),
            ],
            options={
                'verbose_name': '類別標籤',
                'verbose_name_plural': '類別標籤列表',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512, verbose_name='標題')),
                ('author', models.CharField(blank=True, max_length=200, verbose_name='作者')),
                ('s_area_id', models.CharField(blank=True, max_length=100, verbose_name='頻道id')),
                ('content', models.TextField(blank=True, verbose_name='內文')),
                ('post_time', models.DateTimeField(blank=True, null=True, verbose_name='發布時間')),
                ('hash_num', models.CharField(blank=True, max_length=50, verbose_name='雜湊值')),
                ('labeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.labelingjob', verbose_name='所屬任務')),
                ('labels', models.ManyToManyField(blank=True, to='labeling_jobs.Label', verbose_name='被標記標籤')),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件列表',
            },
        ),
    ]
