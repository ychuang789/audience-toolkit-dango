# Generated by Django 3.1.8 on 2021-05-28 17:23

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('modeling_jobs', '0018_auto_20210514_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='termweight',
            options={'ordering': ('modeling_job', 'label', django.db.models.expressions.OrderBy(django.db.models.expressions.F('weight'), descending=True, nulls_last=True), 'term'), 'verbose_name': '詞彙權重', 'verbose_name_plural': '詞彙權重列表'},
        ),
        migrations.AlterField(
            model_name='modelingjob',
            name='feature',
            field=models.CharField(choices=[('id', '文章id'), ('s_id', '來源'), ('s_area_id', '來源網站'), ('title', '標題'), ('author', '作者'), ('content', '內文'), ('post_time', '發文時間')], default='content', max_length=50, verbose_name='特徵欄位'),
        ),
        migrations.AlterField(
            model_name='modelingjob',
            name='model_name',
            field=models.CharField(choices=[('SVM_MODEL', 'SVM'), ('RANDOM_FOREST', '隨機森林'), ('KEYWORD_MODEL', '關鍵字規則'), ('REGEX_MODEL', '正則表達式比對'), ('TERM_WEIGHT_MODEL', '關鍵字權重')], max_length=50, verbose_name='模型類型'),
        ),
    ]
