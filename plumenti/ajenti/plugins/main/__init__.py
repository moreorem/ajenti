from ajenti.api import *
from ajenti.api.http import *
from ajenti.plugins import *


info = PluginInfo(
    title='Core',
    icon='link',
    dependencies=[
    ],
)


def init():
    from . import main
    from . import api
    from . import passwd
    from . import controls_binding
    from . import controls_containers
    from . import controls_simple
    from . import controls_inputs
    from . import controls_dialogs
