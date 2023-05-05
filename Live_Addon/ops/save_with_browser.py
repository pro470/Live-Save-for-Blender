import bpy
from bpy.props import StringProperty


class SaveAsMainfileOperator(bpy.types.Operator):
    bl_idname = "wm.save_as_mainfile_with_browser"
    bl_label = "Save As Mainfile with Browser"
    filepath: StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        # Add ".blend" to the end of the filepath
        filepath_blend = self.filepath + ".blend"
        bpy.ops.wm.save_as_mainfile(filepath=filepath_blend)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
