from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Power',
    icon='bolt',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
    ],
)


def init():
    from . import power
