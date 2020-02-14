from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Munin',
    icon='stethoscope',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
        BinaryDependency('munin-cron'),
        ModuleDependency('BeautifulSoup'),
    ],
)


def init():
    from . import main
    from . import widget
