# Generated by Django 3.2 on 2021-04-07 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labeling_jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='模型種類')),
            ],
            options={
                'verbose_name': '機器學習模型',
                'verbose_name_plural': '機器學習模型列表',
            },
        ),
        migrations.CreateModel(
            name='ModelingJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='模型名稱')),
                ('description', models.CharField(max_length=100, verbose_name='模型敘述')),
                ('is_multi_label', models.BooleanField(verbose_name='是否為多標籤')),
                ('status', models.BooleanField(blank=True, default=False, verbose_name='是否已被訓練過')),
                ('jobRef', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='labeling_jobs.labelingjob')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modeling_jobs.mlmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.FloatField(blank=True, max_length=10, verbose_name='準確率')),
                ('report', models.CharField(max_length=1000, verbose_name='報告')),
                ('models_ref', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='modeling_jobs.modelingjob')),
            ],
        ),
    ]