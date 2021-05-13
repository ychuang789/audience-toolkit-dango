# Generated by Django 3.1.8 on 2021-05-12 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling_jobs', '0023_rule_match_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rule',
            options={'ordering': ('content', 'match_type'), 'verbose_name': '規則', 'verbose_name_plural': '規則列表'},
        ),
        migrations.AlterUniqueTogether(
            name='rule',
            unique_together={('label', 'content', 'match_type')},
        ),
    ]
