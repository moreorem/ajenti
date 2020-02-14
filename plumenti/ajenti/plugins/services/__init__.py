from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Services',
    icon='play',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
    ],
)


def init():
    from . import api

    try:
        import dbus
        
        from . import sm_upstart
        from . import sm_systemd
    except ImportError:
        pass

    from . import sm_sysvinit
    from . import sm_sysvinit_centos
    from . import sm_freebsd
    from . import sm_osx

    from . import main
    from . import widget
    from . import sensor
