from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Scripts',
    icon='play',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
        PluginDependency('terminal'),
    ],
)


def init():
    from . import widget
