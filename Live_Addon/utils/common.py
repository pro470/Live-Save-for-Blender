import bpy
import importlib
from .. import props

props_module1 = props.Live_Addon


# Use props_module.addon here


def module() -> str:
    return props_module1.name


def prefs() -> bpy.types.AddonPreferences:
    return bpy.context.preferences.addons[module()].preferences
