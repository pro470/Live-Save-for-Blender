import bpy
from bpy.types import Operator
from .. import utils
com = utils.common


class LiveSaveLoadNext(Operator):
    bl_idname = 'livesave.load_next'
    bl_label = 'Load Next'
    bl_options = {'INTERNAL'}
    bl_description = 'Load the pre iteration of this file'

    @classmethod
    def poll(cls, context):
        return com.file_path_test(1)

    def execute(self, context):
        com.file_path_version_open(1)
        return {'FINISHED'}
