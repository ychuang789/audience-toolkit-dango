# Generated by Django 3.1.8 on 2021-07-14 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0007_auto_20210714_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rule',
            old_name='labeling_job',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='uploadfilejob',
            old_name='labeling_job',
            new_name='job',
        ),
    ]
