from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    menu = (
        ParentItem('Dashboard', url='/', icon='fa fa-list'),
        ParentItem('Research & Maps', children=[
            ChildItem('LASER', model='survey.laser'),
            ChildItem('Maps', model='survey.map'),
            ChildItem('Research Tracker', model='survey.research'),
        ], icon='fa fa-list'),
        ParentItem('Users', children=[
            ChildItem('Users', model='users.user'),
            ChildItem('Groups', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Right Side Menu', children=[
            ChildItem('Password change', url='admin:password_change'),

        ], align_right=True, icon='fa fa-cog'),
    )
