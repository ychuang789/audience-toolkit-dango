# Generated by Django 3.1.7 on 2021-03-17 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0010_auto_20210317_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='user',
            new_name='created_by',
        ),
    ]