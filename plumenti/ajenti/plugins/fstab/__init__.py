from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Filesystems',
    icon='hdd',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
        FileDependency('/etc/fstab'),
    ],
)


def init():
    from . import main
    from . import widget
    from . import disks
    from . import iops