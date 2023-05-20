import bpy
from .. import props
from . import timer
from . import save_with_browser
from . import detect_mouseclick
from . import save_p_version
from . import load_p_version_pre
from . import load_p_version_post
from . import first_p_version
from . import last_p_version
from . import open_original

addonpref = props.preference.prefs()

CLASSES = [
    timer.LiveSaveMessageHandler,
    save_with_browser.SaveAsMainfileOperator,
    detect_mouseclick.UserActionDetector,
    save_p_version.save_p_version,
    load_p_version_pre.LiveSaveLoadPre,
    load_p_version_post.LiveSaveLoadNext,
    first_p_version.LiveSaveLoadFirst,
    last_p_version.LiveSaveLoadLast,
    open_original.LiveSaveLoadOriginal,
]

register, unregister = bpy.utils.register_classes_factory(CLASSES)
