# Generated by Django 2.2.10 on 2020-02-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0030_auto_20200208_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='other_type',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Please specify if other'),
        ),
    ]
