import os

import bpy
from bpy.types import UIList, Operator


class MY_UL_List(UIList):
    """Demo UIList."""

    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):

        # We could write some code to decide which icon to use here...
        custom_icon = 'OBJECT_DATAMODE'

        # Make sure your code supports all 3 layout types
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon = custom_icon)
            #layout.operator('my_list.open_p_version_index', text="", icon='GREASEPENCIL')

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon = custom_icon)


class LIST_OT_NewItem(Operator):
    """Add a new item to the list."""

    bl_idname = "my_list.new_item"
    bl_label = "Add a new item"

    def execute(self, context):
        bpy.ops.live_save.save_p_version('EXEC_DEFAULT')

        return{'FINISHED'}


class LIST_OT_DeleteItem(Operator):
    """Delete the selected item from the list."""

    bl_idname = "my_list.delete_item"
    bl_label = "Deletes an item"

    @classmethod
    def poll(cls, context):
        return context.window_manager.my_list

    def execute(self, context):
        my_list = context.window_manager.my_list
        index = context.window_manager.list_index
        if os.path.exists(my_list[index].p_version_file_path):
            os.remove(my_list[index].p_version_file_path)

        my_list.remove(index)
        context.window_manager.list_index = min(max(0, index - 1), len(my_list) - 1)

        return{'FINISHED'}


class OPEN_OT_P_VERSION_INDEX(Operator):
    """Open the selected item from the list."""

    bl_idname = "my_list.open_p_version_index"
    bl_label = "Open an item"

    @classmethod
    def poll(cls, context):
        return context.window_manager.my_list

    def execute(self, context):
        my_list = context.window_manager.my_list
        index = context.window_manager.list_index
        if os.path.exists(my_list[index].p_version_file_path):
            bpy.ops.wm.open_mainfile(filepath=my_list[index].p_version_file_path)
        else:
            self.report({'ERROR'}, 'File not found')

        return{'FINISHED'}
"""
class LIST_OT_MoveItem(Operator):
    """"Move an item in the list.""""

    bl_idname = "my_list.move_item"
    bl_label = "Move an item in the list"

    direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""), ('DOWN', 'Down', ""),))

    @classmethod
    def poll(cls, context):
        return context.window_manager.my_list

    def move_index(self):
        """" Move index of an item render queue while clamping it. """"

        index = bpy.context.window_manager.list_index
        list_length = len(bpy.context.window_manager.my_list) - 1  # (index starts at 0)
        new_index = index + (-1 if self.direction == 'UP' else 1)

        bpy.context.window_manager.list_index = max(0, min(new_index, list_length))

    def execute(self, context):
        my_list = context.window_manager.my_list
        index = context.window_manager.list_index

        neighbor = index + (-1 if self.direction == 'UP' else 1)
        my_list.move(neighbor, index)
        self.move_index()

        return{'FINISHED'}
"""
