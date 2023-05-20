import os

import bpy
import importlib
from ..timer import save_version as sv
from .. import props
from .. import utils as u
fph = u.file_path
com = u.common


utils_module = props.preference
# Use props_module.addon here


@bpy.app.handlers.persistent
def auto_start(dummy):
    prefs = utils_module.prefs()
    window_manager = bpy.context.window_manager
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

    if com.file_path_test("first"):
        p_version_folder_path = os.path.dirname(com.new_file_path_func("first"))
        version_files = sorted([f for f in os.listdir(p_version_folder_path) if f.endswith(".blend")])
        for i in range(len(version_files)):
            if len(version_files) == 0:
                break
            new_path = os.path.join(p_version_folder_path, version_files[i])
            list_new_item = bpy.context.window_manager.my_list.add()
            list_new_item.name = version_files[i]
            list_new_item.p_version_file_path = new_path





