# Generated by Django 3.1.8 on 2021-05-13 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0027_auto_20210512_1810'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rule',
            unique_together={('label', 'content', 'match_type')},
        ),
    ]