# Generated by Django 2.2.10 on 2021-02-18 13:48

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0016_delete_infotracker'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('issue_number', models.CharField(blank=True, max_length=100, null=True)),
                ('issue_category', models.CharField(choices=[('Rumor', 'Rumor'), ('Question', 'Question'), ('Trust issue', 'Trust issue'), ('Transparency', 'Transparency'), ('General Concern', 'General Concern')], max_length=50, null=True, verbose_name='Issue Category')),
                ('issue_description', models.TextField(help_text='200 characters max', null=True, verbose_name='Issue description')),
                ('frequency', models.IntegerField(blank=True, default=0, null=True, verbose_name='Frequency')),
                ('target_population', models.CharField(choices=[('All', 'All'), ('Lebanese', 'Lebanese'), ('Foreigner', 'Foreigner'), ('Refugee', 'Refugee'), ('Elderly', 'Elderly'), ('Pregnant', 'Pregnant'), ('People with disabilities', 'People with disabilities'), ('Under 18', 'Under 18')], max_length=100, null=True, verbose_name='Target Population')),
                ('source', models.CharField(choices=[('All', 'All'), ('Poll/Study', 'Poll/Study'), ('Training', 'Training'), ('Community Activity', 'Community Activity'), ('Media', 'Media'), ('Social Media', 'Social Media')], max_length=100, null=True, verbose_name='Source')),
                ('answer', models.TextField(blank=True, help_text='200 characters max', null=True, verbose_name='Answer/Clarification')),
                ('validated_by_technical_committee', models.BooleanField(blank=True, default=False, verbose_name='Validated by Technical Committee')),
                ('validated_by_moph', models.BooleanField(blank=True, default=False, verbose_name='Validated by MOPH')),
                ('dissemination_method', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Community Activity', 'Community Activity'), ('Social Media', 'Social Media'), ('Training', 'Training'), ('Official External Communication', 'Official External Communication')], max_length=100, null=True), blank=True, null=True, size=None, verbose_name='Dissemination method')),
                ('relevant_link', models.URLField(blank=True, null=True, verbose_name='Relevant link')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('reported_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Reported by')),
            ],
            options={
                'verbose_name': 'Concern / Question',
                'verbose_name_plural': 'Concerns / Questions',
                'ordering': ['issue_number'],
            },
        ),
    ]
