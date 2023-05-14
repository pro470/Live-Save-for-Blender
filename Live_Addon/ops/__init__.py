import bpy
from . import timer
from . import save_with_browser
from . import detect_mouseclick
from . import save_p_version
from . import load_p_version_pre
from . import load_p_version_post
from . import first_p_version
from . import last_p_version
from . import open_original


def register():
    bpy.utils.register_class(timer.LiveSaveMessageHandler)
    bpy.utils.register_class(save_with_browser.SaveAsMainfileOperator)
    bpy.utils.register_class(detect_mouseclick.UserActionDetector)
    bpy.utils.register_class(save_p_version.save_p_version)
    bpy.utils.register_class(load_p_version_pre.LiveSaveLoadPre)
    bpy.utils.register_class(load_p_version_post.LiveSaveLoadNext)
    bpy.utils.register_class(first_p_version.LiveSaveLoadFirst)
    bpy.utils.register_class(last_p_version.LiveSaveLoadLast)
    bpy.utils.register_class(open_original.LiveSaveLoadOriginal)


def unregister():
    bpy.utils.unregister_class(timer.LiveSaveMessageHandler)
    bpy.utils.unregister_class(save_with_browser.SaveAsMainfileOperator)
    bpy.utils.unregister_class(detect_mouseclick.UserActionDetector)
    bpy.utils.unregister_class(save_p_version.save_p_version)
    bpy.utils.unregister_class(load_p_version_pre.LiveSaveLoadPre)
    bpy.utils.unregister_class(load_p_version_post.LiveSaveLoadNext)
    bpy.utils.unregister_class(first_p_version.LiveSaveLoadFirst)
    bpy.utils.unregister_class(last_p_version.LiveSaveLoadLast)
    bpy.utils.unregister_class(open_original.LiveSaveLoadOriginal)
