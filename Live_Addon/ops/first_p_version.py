import bpy
from bpy.types import Operator
from .. import utils

com = utils.common


class LiveSaveLoadFirst(Operator):
    bl_idname = 'livesave.load_first'
    bl_label = 'Load Next'
    bl_options = {'INTERNAL'}
    bl_description = 'Load the first iteration of this file'

    @classmethod
    def poll(cls, context):
        return com.file_path_test("first")

    def execute(self, context):
        com.file_path_version_open("first")
        return {'FINISHED'}
