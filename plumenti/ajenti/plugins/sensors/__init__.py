from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Sensors',
    icon='leaf',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
    ],
)


def init():
    from . import hostname
    from . import uptime
    from . import load
    from . import memory
    from . import cpu
