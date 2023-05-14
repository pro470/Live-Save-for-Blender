import bpy
from bpy.types import Operator
from .. import utils
com = utils.common


class LiveSaveLoadOriginal(Operator):
    bl_idname = 'livesave.load_original'
    bl_label = 'Load Next'
    bl_options = {'INTERNAL'}
    bl_description = 'Load the original iteration of this file'

    @classmethod
    def poll(cls, context):
        return com.go_to_original_test()

    def execute(self, context):
        com.go_to_original_open()
        return {'FINISHED'}
