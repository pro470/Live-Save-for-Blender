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
