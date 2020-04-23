# Generated by Django 2.2.10 on 2020-04-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200423_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laser',
            name='status',
            field=models.CharField(blank=True, choices=[('Planned', 'Planned'), ('Ongoing', 'Ongoing'), ('Published', 'Published'), ('Discontinued', 'Discontinued'), ('Finalized', 'Finalized'), ('Finalized (but not yet published--To be published as a print profile)', 'Finalized (but not yet published--To be published as a print profile)'), ('Finalized (but not yet published--To be published as an online profile)', 'Finalized (but not yet published--To be published as an online profile)'), ('Finalized; publication underway', 'Finalized; publication underway'), ('Online profile published', 'Online profile published'), ('Online profile published', 'Online profile published')], default='Planned', max_length=1500, null=True, verbose_name='Status'),
        ),
    ]
