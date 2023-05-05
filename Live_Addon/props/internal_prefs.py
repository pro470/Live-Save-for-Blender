import bpy


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
