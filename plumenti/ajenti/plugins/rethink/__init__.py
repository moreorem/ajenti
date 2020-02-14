from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='RethinkDB',
    icon='table',
    dependencies=[
        PluginDependency('db_common'),
        BinaryDependency('rethinkdb'),
        ModuleDependency('rethinkdb'),
    ],
)


def init():
    from . import api
    from . import main
