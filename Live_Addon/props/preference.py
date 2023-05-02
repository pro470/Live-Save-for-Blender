import bpy
from . import Live_Addon


def module() -> str:
    return Live_Addon.name


def prefs() -> bpy.types.AddonPreferences:
    return bpy.context.preferences.addons[module()].preferences
