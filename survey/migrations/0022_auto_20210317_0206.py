# Generated by Django 2.2.19 on 2021-03-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0021_auto_20210316_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgetracker',
            name='other_population_considerations',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('Elderly', 'Elderly'), ('Pregnant Women', 'Pregnant Women'), ('Breasfeeding Women', 'Breasfeeding Women'), ('People with disabilities', 'People with disabilities'), ('Under 18 ', 'Under 18'), ('People with chronic deseases', 'People with chronic deseases'), ('Social mobilizers: scouts, youth groups, women group, etc...', 'Social mobilizers: scouts, youth groups, women group, etc...'), ('Municipal staff / Crisis cells', 'Municipal staff / Crisis cells'), ('Religious Entities', 'Religious Entities'), ('Frontline workers', 'Frontline workers'), ('Teachers', 'Teachers'), ('NGOs', 'NGOs'), ('CBOs', 'CBOs')], max_length=100, null=True, verbose_name='Other Population Considerations'),
        ),
    ]
