from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SurveyConfig(AppConfig):
    name = 'survey'


class SuitConfig(DjangoSuitConfig):
    menu = (
        ParentItem('Dashboard', url='/', icon='fa fa-list'),
        ParentItem('Survey', children=[
            ChildItem('LASER', model='survey.laser'),
        ], icon='fa fa-list'),
        ParentItem('Users', children=[
            ChildItem('Users', model='users.user'),
            ChildItem('Groups', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Right Side Menu', children=[
            ChildItem('Password change', url='admin:password_change'),

        ], align_right=True, icon='fa fa-cog'),
    )