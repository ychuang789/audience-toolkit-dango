# Generated by Django 3.1.8 on 2021-04-20 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0004_auto_20210420_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='type',
            new_name='document_type',
        ),
    ]