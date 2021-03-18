# Generated by Django 3.1.7 on 2021-03-16 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labeling_jobs', '0005_auto_20210316_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='document_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='document_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='job_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='job_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='label',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='label_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='label',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='label_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.job', verbose_name='所屬任務'),
        ),
        migrations.AlterField(
            model_name='document',
            name='labels',
            field=models.ManyToManyField(to='labeling_jobs.Label', verbose_name='被標記標籤'),
        ),
        migrations.AlterField(
            model_name='label',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling_jobs.job', verbose_name='所屬任務'),
        ),
    ]