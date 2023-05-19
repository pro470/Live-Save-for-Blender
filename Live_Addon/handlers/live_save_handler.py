import bpy
import os
import shutil
from .. import props


@bpy.app.handlers.persistent
def on_save_post_handler(dummy):
    file_path12 = bpy.context.window_manager.my_addon_props.file_path
    if bpy.data.filepath:
        if os.path.exists(file_path12):
            os.remove(file_path12)
