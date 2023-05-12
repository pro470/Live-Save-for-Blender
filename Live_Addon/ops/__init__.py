import bpy
from . import timer
from . import save_with_browser
from . import detect_mouseclick
from . import save_p_version


def register():
    bpy.utils.register_class(timer.LiveSaveMessageHandler)
    bpy.utils.register_class(save_with_browser.SaveAsMainfileOperator)
    bpy.utils.register_class(detect_mouseclick.UserActionDetector)
    bpy.utils.register_class(save_p_version.save_p_version)


def unregister():
    bpy.utils.unregister_class(timer.LiveSaveMessageHandler)
    bpy.utils.unregister_class(save_with_browser.SaveAsMainfileOperator)
    bpy.utils.unregister_class(detect_mouseclick.UserActionDetector)
    bpy.utils.unregister_class(save_p_version.save_p_version)
