from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Test',
    icon=None,
    dependencies=[
        PluginDependency('main'),
    ],
)


def init():
    from . import simple.main
    from . import events.main
    from . import notifications.main
    from . import binder.main
    from . import http.http
    from . import classconfig.main
