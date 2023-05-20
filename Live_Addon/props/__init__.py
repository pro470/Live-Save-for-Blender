import bpy
from . import Live_Addon
from . import prefs
from . import preference
from . import internal_prefs
from ..utils import common
from bpy.props import StringProperty, IntProperty, CollectionProperty


def register():
    bpy.utils.register_class(Live_Addon.LiveSaveProps)
    bpy.utils.register_class(prefs.LiveSavePreferences)
    bpy.utils.register_class(internal_prefs.MyAddonProperties)
    bpy.utils.register_class(internal_prefs.ListItem)


    bpy.types.WindowManager.LiveSave = bpy.props.PointerProperty(type=Live_Addon.LiveSaveProps)
    bpy.types.WindowManager.my_addon_props = bpy.props.PointerProperty(type=internal_prefs.MyAddonProperties)
    bpy.types.WindowManager.my_list = CollectionProperty(type=internal_prefs.ListItem)
    bpy.types.WindowManager.list_index = IntProperty(name="Index for my_list", default=0)



def unregister():
    del bpy.types.WindowManager.my_list
    del bpy.types.WindowManager.list_index
    del bpy.types.WindowManager.my_addon_props
    del bpy.types.WindowManager.LiveSave

    bpy.utils.unregister_class(internal_prefs.ListItem)
    bpy.utils.unregister_class(internal_prefs.MyAddonProperties)
    bpy.utils.unregister_class(prefs.LiveSavePreferences)
    bpy.utils.unregister_class(Live_Addon.LiveSaveProps)

