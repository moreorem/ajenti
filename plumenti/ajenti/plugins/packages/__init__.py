from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Package manager',
    icon='gift',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('terminal')
    ],
)


def init():
    from . import main
    from . import pm_apt
    from . import pm_bsd
    from . import pm_yum
    from . import pm_pacman
    from . import pm_urpmi
    from . import pm_macports
    from . import installer