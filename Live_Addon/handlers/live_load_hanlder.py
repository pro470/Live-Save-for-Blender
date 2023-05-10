import bpy
import importlib
from ..timer import save_version as sv
from .. import props


utils_module = props.preference
# Use props_module.addon here


@bpy.app.handlers.persistent
def auto_start(dummy):
    prefs = utils_module.prefs()
    if prefs.is_enabled:
        bpy.ops.wm.live_save_message_handler('EXEC_DEFAULT')
    else:
        if bpy.context.window_manager.my_addon_props.is_enabled:
            if not bpy.app.timers.is_registered(sv.save_version):
                bpy.app.timers.register(sv.save_version, first_interval=bpy.context.window_manager.my_addon_props.version_timer, persistent=True)
