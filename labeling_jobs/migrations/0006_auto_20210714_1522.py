# Generated by Django 3.1.8 on 2021-07-14 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0005_auto_20210714_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='job',
            new_name='labeling_job',
        ),
        migrations.RenameField(
            model_name='rule',
            old_name='job',
            new_name='labeling_job',
        ),
        migrations.RenameField(
            model_name='uploadfilejob',
            old_name='job',
            new_name='labeling_job',
        ),
    ]
