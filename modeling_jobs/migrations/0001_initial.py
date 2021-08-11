# Generated by Django 3.1.13 on 2021-07-23 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labeling_jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelingJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='模型名稱')),
                ('description', models.CharField(max_length=100, verbose_name='模型敘述')),
                ('is_multi_label', models.BooleanField(default=False, verbose_name='是否為多標籤')),
                ('model_name', models.CharField(choices=[('SVM_MODEL', 'SVM'), ('RANDOM_FOREST', '隨機森林'), ('KEYWORD_MODEL', '關鍵字規則'), ('REGEX_MODEL', '正則表達式比對'), ('TERM_WEIGHT_MODEL', '詞彙權重模型')], max_length=50, verbose_name='模型類型')),
                ('feature', models.CharField(choices=[('id', '文章id'), ('s_id', '來源'), ('s_area_id', '來源網站'), ('title', '標題'), ('author', '作者'), ('content', '內文'), ('post_time', '發文時間')], default='content', max_length=50, verbose_name='特徵欄位')),
                ('job_status', models.CharField(choices=[('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='模型訓練狀態')),
                ('error_message', models.TextField(null=True, verbose_name='錯誤訊息')),
                ('ext_test_status', models.CharField(choices=[('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='模型測試狀態')),
                ('model_path', models.CharField(blank=True, max_length=100, verbose_name='模型存放位置')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='建立者')),
                ('jobRef', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='labeling_jobs.labelingjob', verbose_name='使用資料')),
            ],
            options={
                'verbose_name': '模型訓練任務',
                'verbose_name_plural': '模型訓練任務列表',
            },
        ),
        migrations.CreateModel(
            name='UploadModelJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload_files', verbose_name='檔案')),
                ('job_status', models.CharField(choices=[('wait', '等待中'), ('processing', '處理中'), ('break', '中斷'), ('error', '錯誤'), ('done', '完成')], default='wait', max_length=20, verbose_name='任務狀態')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('modeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeling_jobs.modelingjob', verbose_name='所屬任務')),
            ],
            options={
                'verbose_name': '模型上傳任務',
                'verbose_name_plural': '模型上傳任務列表',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_type', models.CharField(choices=[('train', '訓練資料'), ('dev', '驗證資料'), ('test', '測試資料'), ('ext_test', '額外測試資料')], default=None, max_length=10, null=True)),
                ('accuracy', models.FloatField(blank=True, max_length=10, verbose_name='準確率')),
                ('report', models.CharField(max_length=1000, verbose_name='報告')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('modeling_job', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='modeling_jobs.modelingjob')),
            ],
            options={
                'verbose_name': '驗證報告',
                'verbose_name_plural': '驗證報告列表',
            },
        ),
        migrations.CreateModel(
            name='EvalPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.document', verbose_name='預測文件')),
                ('prediction_labels', models.ManyToManyField(to='labeling_jobs.Label', verbose_name='預測標籤')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeling_jobs.report', verbose_name='驗證報告')),
            ],
            options={
                'verbose_name': '驗證標記',
                'verbose_name_plural': '驗證標記列表',
            },
        ),
        migrations.CreateModel(
            name='TermWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20, verbose_name='詞彙')),
                ('weight', models.FloatField(verbose_name='權重分數')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.label', verbose_name='所屬標籤')),
                ('modeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeling_jobs.modelingjob', verbose_name='模型訓練任務')),
            ],
            options={
                'verbose_name': '詞彙權重',
                'verbose_name_plural': '詞彙權重列表',
                'ordering': ('modeling_job', 'label', django.db.models.expressions.OrderBy(django.db.models.expressions.F('weight'), descending=True, nulls_last=True), 'term'),
                'unique_together': {('modeling_job', 'term', 'label')},
            },
        ),
    ]
