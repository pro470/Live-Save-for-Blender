import bpy
from . import save_version
from .. import props



def register():
    if bpy.context.window_manager.my_addon_props.is_enabled_version:
        if not bpy.app.timers.is_registered(save_version.save_version):
            interval = bpy.context.window_manager.my_addon_props.version_timer
            bpy.app.timers.register(save_version.save_version, first_interval=interval, persistent=True)


def unregister():
    if bpy.app.timers.is_registered(save_version.save_version):
        bpy.app.timers.unregister(save_version.save_version)
