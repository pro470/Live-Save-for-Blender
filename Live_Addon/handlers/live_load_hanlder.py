import bpy
import importlib
from ..timer import save_version as sv
from .. import props
from .. import utils as u
fph = u.file_path


utils_module = props.preference
# Use props_module.addon here


@bpy.app.handlers.persistent
def auto_start(dummy):
    prefs = utils_module.prefs()
    if prefs.auto_start_save:
        print("auto start save")
        file_path = fph.create_new_file_path()
        bpy.ops.wm.save_as_mainfile(filepath=file_path)
    if prefs.is_enabled:
        bpy.ops.wm.live_save_message_handler('EXEC_DEFAULT')
        bpy.ops.wm.user_action_detector('EXEC_DEFAULT')
    if bpy.context.window_manager.my_addon_props.is_enabled_version:
        if not bpy.app.timers.is_registered(sv.save_version):
            bpy.app.timers.register(sv.save_version, first_interval=bpy.context.window_manager.my_addon_props.version_timer, persistent=True)

