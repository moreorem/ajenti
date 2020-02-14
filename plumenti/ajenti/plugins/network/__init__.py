from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Network',
    icon='exchange',
    dependencies=[
        PluginDependency('main'),
        PluginDependency('dashboard'),
    ],
)


def init():
    from . import widget
    from . import api
    from . import main
    from . import nctp_linux
    from . import nc_debian
    from . import nc_centos
    from . import ncs_linux_basic
    from . import ncs_linux_ipv4
    from . import ncs_linux_dhcp
    from . import ncs_linux_ifupdown
