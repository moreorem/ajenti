from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Dashboard',
    icon='dashboard',
    dependencies=[
        PluginDependency('main')
    ],
)


def init():
    from . import dash
    from . import api
    from . import welcome
    from . import text
