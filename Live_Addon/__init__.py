from . import props
from . import ops
from . import handlers
from . import ui
from . import timer
import bpy
import os


def register():
    props.register()
    ops.register()
    timer.register()
    handlers.register()
    ui.register()


def unregister():
    ui.unregister()
    handlers.unregister()
    timer.unregister()
    ops.unregister()
    file_path12 = bpy.context.window_manager.my_addon_props.file_path
    if os.path.exists(file_path12):
        os.remove(file_path12)
    props.unregister()
