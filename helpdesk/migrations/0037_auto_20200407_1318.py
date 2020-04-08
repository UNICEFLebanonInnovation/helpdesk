# Generated by Django 2.2.10 on 2020-04-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0036_auto_20200312_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='report_type',
            field=models.CharField(blank=True, choices=[('', '---------'), ('Complaint on vaccine storage, provision and disposal', 'Complaint on vaccine storage, provision and disposal'), ('Complaint on vaccinator s skills and visibility (ID/ brand - logo of the campaign should be visible)', "Complaint on vaccinator's skills and visibility (ID/ brand – logo of the campaign should be visible)"), ('Complaint on proper and timely preparation of the community before vaccination', 'Complaint on proper and timely preparation of the community before vaccination'), ('Report on Refusal of vaccination by a community or an institution', 'Report on Refusal of vaccination by a community or an institution'), ('Misconceptions and rumors', 'Misconceptions and rumors'), ('Other challenges or complaints', 'Other challenges or complaints')], max_length=1500, null=True, verbose_name='Report Type'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sub_report_type',
            field=models.CharField(blank=True, choices=[('', '---------'), ('Medical reasons ', 'Medical reasons'), ('No trust in the vaccine provided ', 'No trust in the vaccine provided'), ('No trust in the team providing the vaccines', 'No trust in the team providing the vaccines'), ('Child already vaccinated', 'Child already vaccinated'), ('Based on the recommendation of the pediatric/ physician', 'Based on the recommendation of the pediatric/ physician'), ('Religious reasons', 'Religious reasons'), ('Anti- vaccination movement ', 'Anti- vaccination movement'), ('Other/ specify', 'Other/ specify')], max_length=1500, null=True, verbose_name='Please specify reasons n the narrative as per the following'),
        ),
    ]