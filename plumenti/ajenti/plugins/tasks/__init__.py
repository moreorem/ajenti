from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Tasks',
    icon='cog',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('cron'),
    ],
)


def init():
    from . import api
    from . import manager
    from . import main
    from . import tasks
