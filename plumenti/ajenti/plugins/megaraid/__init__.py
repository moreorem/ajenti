from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='RAID',
    description='LSI MegaRAID status display',
    icon='hdd',
    dependencies=[
        PluginDependency('main'),
        FileDependency('/opt/MegaRAID/MegaCli/MegaCli'),
    ],
)


def init():
    from . import api
    from . import main
    from . import widget
