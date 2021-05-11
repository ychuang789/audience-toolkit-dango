# Generated by Django 3.1.8 on 2021-04-20 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labeling_jobs', '0006_remove_uploadfilejob_delimiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='human_labels',
            field=models.ManyToManyField(blank=True, related_name='human_label', to='labeling_jobs.Label', verbose_name='人員標記標籤'),
        ),
        migrations.AlterField(
            model_name='document',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='ground_truth_label', to='labeling_jobs.Label', verbose_name='正確標籤'),
        ),
        migrations.CreateModel(
            name='HumanLabeling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.document', verbose_name='文件')),
                ('human_labels', models.ManyToManyField(to='labeling_jobs.Label', verbose_name='標記標籤')),
                ('labeling_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.labelingjob', verbose_name='標記任務')),
            ],
            options={
                'verbose_name': '人員標記',
                'verbose_name_plural': '人員標記列表',
            },
        ),
    ]