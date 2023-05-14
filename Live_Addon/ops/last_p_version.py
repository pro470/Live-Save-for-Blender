import bpy
from bpy.types import Operator
from .. import utils
com = utils.common


class LiveSaveLoadLast(Operator):
    bl_idname = 'livesave.load_last'
    bl_label = 'Load Next'
    bl_options = {'INTERNAL'}
    bl_description = 'Load the last iteration of this file'

    @classmethod
    def poll(cls, context):
        return com.file_path_test("last")

    def execute(self, context):
        com.file_path_version_open("last")
        return {'FINISHED'}
