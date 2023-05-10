import re

from . import props
from . import ops
from . import handlers
from . import ui
from . import timer
from . import utils
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
    blend_match = r"\.blend"
    matched_blend = re.search(blend_match, file_path12)
    # when it is not a folder and it is a blend file
    if not os.path.isdir(file_path12) and matched_blend and os.path.exists(file_path12):
        os.remove(file_path12)
    props.unregister()
