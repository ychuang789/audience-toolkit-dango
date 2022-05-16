# Generated by Django 3.1.13 on 2022-05-05 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documenting_jobs', '0003_auto_20220505_1101'),
        ('modeling_jobs', '0007_auto_20220126_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelingjob',
            name='docRef',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='documenting_jobs.documentingjob', verbose_name='模型資料來源'),
        ),
        migrations.AlterField(
            model_name='modelingjob',
            name='model_name',
            field=models.CharField(choices=[('SVM_MODEL', 'SVM'), ('RANDOM_FOREST_MODEL', '隨機森林'), ('KEYWORD_MODEL', '關鍵字規則'), ('REGEX_MODEL', '正則表達式比對'), ('TERM_WEIGHT_MODEL', '詞彙權重模型')], max_length=50, verbose_name='模型類型'),
        ),
    ]