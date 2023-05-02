import bpy
import importlib

utils_module = importlib.import_module("Live Save.Live_Addon.props.preference")
# Use props_module.addon here


@bpy.app.handlers.persistent
def auto_start(dummy):
    prefs = utils_module.prefs()
    if prefs.is_enabled:
        bpy.ops.wm.live_save_message_handler('EXEC_DEFAULT')
