# Generated by Django 2.2.10 on 2020-04-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20200423_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laser',
            name='estimated_cost',
            field=models.FloatField(blank=True, default=0.0, help_text='$', null=True, verbose_name='Estimated cost'),
        ),
        migrations.AlterField(
            model_name='laser',
            name='title',
            field=models.CharField(blank=True, default='No Title', max_length=500, null=True, verbose_name='Title'),
        ),
    ]
