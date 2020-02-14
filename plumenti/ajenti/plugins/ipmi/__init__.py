from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='IPMI',
    description='Intel power management interface widgets',
    icon='dashboard',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
        BinaryDependency('ipmitool')
    ],
)


def init():
    from . import widget
    from . import sensor