# Generated by Django 2.2.19 on 2021-08-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0041_auto_20210812_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgetracker',
            name='answer',
            field=models.TextField(blank=True, help_text='150 characters max', max_length=150, null=True, verbose_name='Answer/Clarification'),
        ),
    ]