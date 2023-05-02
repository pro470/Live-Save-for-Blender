import bpy
import importlib

props_module1 = importlib.import_module("Live Save.Live_Addon.props.Live_Addon")


# Use props_module.addon here


def module() -> str:
    return props_module1.name


def prefs() -> bpy.types.AddonPreferences:
    return bpy.context.preferences.addons[module()].preferences
