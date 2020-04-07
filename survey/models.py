from django.db import models
from model_utils.models import TimeStampedModel


class LASER(TimeStampedModel):

    STATUS_CHOICES = (
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Published', 'Published'),
        ('Discontinued', 'Discontinued'),
        ('Finalized', 'Finalized'),
        ('Finalized (but not yet published--To be published as a print profile)',
         'Finalized (but not yet published--To be published as a print profile)'),
        ('Finalized (but not yet published--To be published as an online profile)',
         'Finalized (but not yet published--To be published as an online profile)'),
        ('Finalized; publication underway', 'Finalized; publication underway'),
        ('Online profile published', 'Online profile published'),
        ('Online profile published', 'Online profile published'),
    )

    CATEGORY_CHOICES = (
        ('Evaluation', 'Evaluation'),
        ('Assessment', 'Assessment'),
        ('Survey', 'Survey'),
        ('Study', 'Study'),
    )

    laser_id = models.CharField(
        'LASER_ID',
        max_length=254,
        unique=True,
    )

    organization = models.CharField(
        'Organization Name',
        max_length=1500,
        blank=True,
        null=True,
    )

    focal_point_contact = models.CharField(
        'Focal Point Contact',
        max_length=1500,
        blank=True,
        null=True,
    )

    title = models.CharField(
        'Title',
        max_length=500,
    )

    description = models.TextField(
        'Brief description of objectives',
        blank=True,
        null=True,
    )

    status = models.CharField(
        'Status',
        max_length=1500,
        choices=STATUS_CHOICES,
    )

    population_targeted = models.CharField(
        'Population Targeted',
        max_length=1500,
    )

    sectors_covered = models.CharField(
        'Sectors covered',
        max_length=1500,
    )

    report_link = models.URLField(
        'Link to the report',
        blank=True,
        null=True,
        max_length=1500,
    )

    required_followup = models.CharField(
        'If marked as planned or ongoing, when would you like us to follow up with you?',
        blank=True,
        null=True,
        max_length=1500,
    )

    published_date = models.DateField(
        'Published date/Date of last update',
        max_length=1500,
        blank=True,
        null=True,
    )

    publication_date = models.DateField(
        'Date of publication (actual/expected)',
        max_length=1500,
        blank=True,
        null=True,
    )

    estimated_cost = models.FloatField(
        'Estimated cost',
        blank=True, null=True,
        help_text='$'
    )

    category = models.CharField(
        'Category',
        max_length=500,
        blank=True,
        null=True,
        choices=CATEGORY_CHOICES,
    )

    evaluation_type = models.CharField(
        'If evaluation, what type?',
        max_length=500,
        blank=True,
        null=True,
        choices=(
            ('Thematic', 'Thematic'),
            ('UNDAF', 'UNDAF'),
            ('Country Programme', 'Country Programme'),
            ('Outcome', 'Outcome'),
            ('Project', 'Project'),
        ),
    )

    geographical_focus = models.CharField(
        'Geographical Focus',
        max_length=500,
        blank=True,
        null=True
    )

    UNSF_outcome = models.CharField(
        'UNSF Outcome',
        max_length=500,
        blank=True,
        null=True
    )

    section = models.CharField(
        'Section',
        max_length=500,
        blank=True,
        null=True
    )

    class Meta:
        get_latest_by = "created"
        ordering = ('laser_id',)
        verbose_name = 'LASER'
        verbose_name_plural = 'LASER'

    def __str__(self):
        return '%s %s' % (self.laser_id, self.title)
