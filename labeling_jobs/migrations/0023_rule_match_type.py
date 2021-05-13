# Generated by Django 3.1.8 on 2021-05-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0022_auto_20210503_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='match_type',
            field=models.CharField(choices=[('start', '比對開頭'), ('end', '比對結尾'), ('exactly', '完全一至'), ('partially', '部分吻合')], default='partially', max_length=20, verbose_name='比對方式'),
        ),
    ]
