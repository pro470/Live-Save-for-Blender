import bpy
from .. import utils
from bpy.types import Operator
com = utils.common


class LiveSaveLoadPre(Operator):
    bl_idname = 'livesave.load_pre'
    bl_label = 'Load Pre'
    bl_options = {'INTERNAL'}
    bl_description = 'Load the pre iteration of this file'

    @classmethod
    def poll(cls, context):
        return com.file_path_test(-1)

    def execute(self, context):
        com.file_path_version_open(-1)
        return {'FINISHED'}
