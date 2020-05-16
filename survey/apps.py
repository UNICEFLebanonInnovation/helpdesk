from django.apps import AppConfig
from django.conf import settings
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SurveyConfig(AppConfig):
    name = 'survey'


class SuitConfig(DjangoSuitConfig):
    menu = (
        ParentItem('Users', children=[
            ChildItem('Users', model='auth.user'),
            ChildItem('Groups', 'auth.group'),
        ], icon='fa fa-users'),
    )

    if settings.MODULE_SURVEY_ACTIVE:
        menu = menu + (
            ParentItem('Survey', children=[
                ChildItem('LASER', model='survey.laser'),
                ChildItem('Maps', model='survey.map'),
            ], icon='fa fa-list'),
        )

    if settings.MODULE_HELPDESK_ACTIVE:
        menu = menu + (
            ParentItem('Dashboard', url='/', icon='fa fa-list'),
            ParentItem('Helpdesk', children=[
                ChildItem('Queue', model='helpdesk.queue'),
                ChildItem('Tickets', model='helpdesk.ticket'),
                ChildItem('Custom fields', model='helpdesk.customfield'),
                ChildItem('E-mail templates', model='helpdesk.emailtemplate'),
                ChildItem('Escalation exclusions', model='helpdesk.escalationexclusion'),
                ChildItem('Follow-ups', model='helpdesk.followup'),
                ChildItem('Ignored e-mail addresses', model='helpdesk.ignoredemail'),
                ChildItem('Knowledge base categories', model='helpdesk.kbasecategory'),
                ChildItem('Knowledge base items', model='helpdesk.kbitem'),
                ChildItem('Pre-set replies', model='helpdesk.presetreply'),
            ], icon='fa fa-list'),
        )

