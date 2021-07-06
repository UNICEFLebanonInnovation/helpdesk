# Generated by Django 2.2.19 on 2021-07-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0037_auto_20210706_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgetracker',
            name='answer',
            field=models.TextField(blank=True, help_text='100 characters max', max_length=100, null=True, verbose_name='Answer/Clarification'),
        ),
        migrations.AlterField(
            model_name='knowledgetracker',
            name='issue_description',
            field=models.TextField(help_text='100 characters max', max_length=100, null=True, verbose_name='Issue description'),
        ),
    ]
