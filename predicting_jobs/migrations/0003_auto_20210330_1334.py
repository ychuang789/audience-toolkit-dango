# Generated by Django 3.1.7 on 2021-03-30 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modeling_jobs', '0002_auto_20210326_1740'),
        ('predicting_jobs', '0002_auto_20210330_1330'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplyModel',
            new_name='ApplyingModel',
        ),
    ]
