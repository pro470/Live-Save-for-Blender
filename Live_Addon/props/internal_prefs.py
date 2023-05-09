import bpy
from ..timer import save_version


class MyAddonProperties(bpy.types.PropertyGroup):
    file_path: bpy.props.StringProperty(
        name="File Path",
        description="Enter file path",
        default="Bernd"
    )
    exec_count: bpy.props.IntProperty(
        name="exec count",
        description='The count or the the undo/redo',
        default=0,
        step=1
    )

    mouse_detect: bpy.props.BoolProperty(
        name="Detects mouse click",
        description="when you release the mouse it will set is to true",
        default=False
    )

    version_timer: bpy.props.FloatProperty(
        name="Timer Version",
        description="A slider for the timers",
        default=1.0,
        min=1,
        max=60*60,
        soft_min=2,
        soft_max=600,
        step=1,
        precision=2,
        update=save_version.update_version_timer
    )

    is_enabled_version: bpy.props.BoolProperty(
        name="Enable Version",
        description="Enable or disable Version",
        default=True,
        update=save_version.update_version_bool
    )

    version_count: bpy.props.IntProperty(
        name="Version Number",
        description='The count of the version',
        default=1,
        step=1,
        min=1
    )
