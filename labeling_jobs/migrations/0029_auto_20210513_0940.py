# Generated by Django 3.1.8 on 2021-05-13 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0028_auto_20210513_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelingjob',
            name='job_data_type',
            field=models.CharField(choices=[('supervise_model', '監督式學習模型'), ('rule_base', '規則模型'), ('regex', '正則表達式模型'), ('term_weight', '詞彙權重模型')], default='supervise_model', max_length=20, verbose_name='任務類型'),
        ),
    ]