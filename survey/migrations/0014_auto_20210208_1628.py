# Generated by Django 2.2.10 on 2021-02-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_infotracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotracker',
            name='issue_description',
            field=models.TextField(null=True, verbose_name='Issue description'),
        ),
    ]
