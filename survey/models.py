import datetime
from django.db import models
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField


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
        blank=True,
        null=True,
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
        blank=True,
        null=True,
        default='No Title'
    )

    description = models.TextField(
        'Brief description of objectives',
        blank=True, null=True,
    )

    status = models.CharField(
        'Status',
        max_length=1500,
        choices=STATUS_CHOICES,
        blank=True, null=True,
        default='Planned'
    )

    population_targeted = models.CharField(
        'Population Targeted',
        max_length=1500,
        blank=True, null=True,
    )

    sectors_covered = models.CharField(
        'Sectors covered',
        max_length=1500,
        blank=True, null=True,
    )

    report_link = models.CharField(
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

    published_date = models.CharField(
        'Published date/Date of last update',
        max_length=1500,
        blank=True,
        null=True,
    )

    publication_date = models.CharField(
        'Date of publication (actual/expected)',
        max_length=1500,
        blank=True,
        null=True,
    )

    estimated_cost = models.CharField(
        'Estimated cost',
        max_length=1500,
        blank=True, null=True,
        help_text='$',
        default=0.0
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


class Research(TimeStampedModel):

    TYPE_CHOICES = (
        ('Qualitative', 'Qualitative'),
        ('Quantitative', 'Quantitative'),
        ('Mixed', 'Mixed'),
        ('Desk Review', 'Desk Review'),
    )

    SECTOR_CHOICES = (
        ('Child Protection', 'Child Protection'),
        ('Health and Nutrition', 'Health and Nutrition'),
        ('Education', 'Education'),
        ('WASH', 'WASH'),
        ('Social Policy', 'Social Policy'),
        ('Cross-sectoral (Gender, Disability, Youth, etc.)', 'Cross-sectoral (Gender, Disability, Youth, etc.)'),
    )

    GEOGRAPHICAL_CHOICES = (
        ('Governorate', 'Governorate'),
        ('District', 'District'),
        ('Neighborhood/Village', 'Neighborhood/Village'),
        ('National', 'National'),
    )

    research_id = models.CharField(
        'RESEARCH_ID',
        max_length=254,
        blank=True,
        null=True,
    )

    title = models.CharField(
        'Title',
        max_length=500,
        blank=False,
        null=False,
        help_text=u'The full title of the research'
    )

    publication_year = models.CharField(
        'Year of publication',
        max_length=1500,
        blank=False,
        null=False,
        help_text=u'The year the research was published or made available for public use'
    )

    organizations = models.CharField(
        'Organization(s)',
        max_length=1500,
        blank=False,
        null=False,
        help_text=u'The organization managing the research'
    )

    researchers = models.CharField(
        'Researcher(s)',
        max_length=1500,
        blank=False,
        null=False,
        help_text=u'The company or consultant(s) conducting the research'
    )

    type = models.CharField(
        'Type of research',
        max_length=500,
        blank=False,
        null=False,
        choices=TYPE_CHOICES,
    )

    main_sector = models.CharField(
        'Main Sector',
        max_length=500,
        blank=False,
        null=False,
        choices=SECTOR_CHOICES,
    )

    geographical_coverage = models.CharField(
        'Geographical Coverage',
        max_length=500,
        blank=False,
        null=False,
        choices=GEOGRAPHICAL_CHOICES,
    )

    description = models.TextField(
        'Description/Abstract',
        blank=True, null=True,
        max_length=250,
        help_text=u'A brief narative on the research objectives, methodology, and findings. 250 characters maximum'
    )

    report_link = models.URLField(
        'Link to Report',
        blank=True,
        null=True,
        max_length=2500,
        help_text=u'URL link to access the report'
    )

    recommendations = HTMLField(
        'Recommendations',
        blank=True, null=True,
        help_text=u'Copy and paste or summarize the recommendations that the research study found'
    )

    planned_actions = HTMLField(
        'Planned Action',
        blank=True, null=True,
        help_text=u'Note down the planned actions by either UNICEF or any other entity'
    )

    taken_actions = HTMLField(
        'Taken Action',
        blank=True, null=True,
        help_text=u'Note down the taken actions by either UNICEF or any other entity'
    )

    class Meta:
        get_latest_by = "created"
        ordering = ('research_id',)
        verbose_name = 'Research'
        verbose_name_plural = 'Research'

    def __str__(self):
        return '%s %s' % (self.research_id, self.title)

    def save(self, **kwargs):
        if not self.research_id:
            year = datetime.date.today().year
            month = '{0:02d}'.format(datetime.date.today().month)
            objects = list(Research.objects.filter(
                created__year=year,
            ).order_by('created').values_list('id', flat=True))
            sequence = '{0:02d}'.format(objects.index(self.id) + 1 if self.id in objects else len(objects) + 1)
            self.research_id = '{}{}-{}'.format(
                year,
                month,
                sequence
            )

        super(Research, self).save(**kwargs)


class Map(TimeStampedModel):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    status = models.CharField(
        'Status',
        max_length=1500,
        choices=(
            ('Draft', 'Draft'),
            ('In progress', 'In progress'),
            ('Completed', 'Completed'),
        ),
        blank=True, null=True,
        default='Draft'
    )

    class Meta:
        ordering = ['name']

    def __unicode__(self):
            return self.name
