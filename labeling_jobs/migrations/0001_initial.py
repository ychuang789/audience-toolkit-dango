# Generated by Django 3.1.8 on 2021-07-12 15:17

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
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512, verbose_name='標題')),
                ('author', models.CharField(blank=True, max_length=200, verbose_name='作者')),
                ('s_id', models.CharField(blank=True, max_length=100, verbose_name='來源')),
                ('s_area_id', models.CharField(blank=True, max_length=100, verbose_name='來源網站')),
                ('content', models.TextField(blank=True, verbose_name='內文')),
                ('post_time', models.DateTimeField(blank=True, null=True, verbose_name='發布時間')),
                ('hash_num', models.CharField(blank=True, max_length=50, verbose_name='雜湊值')),
                ('document_type', models.CharField(choices=[('train', '訓練資料'), ('dev', '驗證資料'), ('test', '測試資料'), ('ext_test', '額外測試資料')], default=None, max_length=10, null=True)),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件列表',
            },
        ),
        migrations.CreateModel(
            name='LabelingJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Job', max_length=100, verbose_name='標記工作名稱')),
                ('description', models.TextField(verbose_name='定義與說明')),
                ('is_multi_label', models.BooleanField(default=False, verbose_name='是否屬於多標籤')),
                ('job_data_type', models.CharField(choices=[('supervise_model', '監督式學習模型'), ('rule_base', '關鍵字規則模型'), ('regex', '正則表達式模型'), ('term_weight', '詞彙權重模型')], default='supervise_model', max_length=20, verbose_name='任務類型')),
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
            options={
                'verbose_name': '文件上傳任務',
                'verbose_name_plural': '文件上傳任務列表',
            },
        ),
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sample Data', max_length=100, verbose_name='範例資料名稱')),
                ('description', models.TextField(verbose_name='定義與說明')),
                ('job_data_type', models.CharField(choices=[('supervise_model', '監督式學習模型'), ('rule_base', '關鍵字規則模型'), ('regex', '正則表達式模型'), ('term_weight', '詞彙權重模型')], default=None, max_length=20, null=True, verbose_name='任務類型')),
                ('file', models.FileField(upload_to='sample_data_files', verbose_name='檔案')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '範例資料',
                'verbose_name_plural': '範例資料列表',
                'ordering': ('created_at', 'name', 'job_data_type'),
            },
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
            name='HumanLabeling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.document', verbose_name='文件')),
                ('human_labels', models.ManyToManyField(to='labeling_jobs.Label', verbose_name='標記標籤')),
                ('labeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.labelingjob', verbose_name='標記任務')),
            ],
            options={
                'verbose_name': '人員標記',
                'verbose_name_plural': '人員標記列表',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='labeling_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.labelingjob', verbose_name='所屬任務'),
        ),
        migrations.AddField(
            model_name='document',
            name='labels',
            field=models.ManyToManyField(blank=True, to='labeling_jobs.Label', verbose_name='正確標籤'),
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='規則內文')),
                ('rule_type', models.CharField(choices=[('keyword', '關鍵字'), ('regex', '正則表達式'), ('term_weight', '詞彙加權')], default='keyword', max_length=20, verbose_name='規則類型')),
                ('match_type', models.CharField(choices=[('start', '比對開頭'), ('end', '比對結尾'), ('exactly', '完全一致'), ('partially', '部分吻合')], default='partially', max_length=20, verbose_name='比對方式')),
                ('score', models.FloatField(default=1, verbose_name='命中分數')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.label', verbose_name='標籤')),
                ('labeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.labelingjob')),
            ],
            options={
                'verbose_name': '規則',
                'verbose_name_plural': '規則列表',
                'ordering': ('content', 'match_type'),
                'unique_together': {('label', 'content', 'match_type')},
            },
        ),
    ]
