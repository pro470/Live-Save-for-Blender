import bpy
from . import timer
from . import save_with_browser


def register():
    bpy.utils.register_class(timer.LiveSaveMessageHandler)
    bpy.utils.register_class(save_with_browser.SaveAsMainfileOperator)


def unregister():
    bpy.utils.unregister_class(timer.LiveSaveMessageHandler)
    bpy.utils.unregister_class(save_with_browser.SaveAsMainfileOperator)
