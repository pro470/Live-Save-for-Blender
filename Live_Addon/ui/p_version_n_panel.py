import bpy
import os
import datetime
from .. import props
from .. import utils


class LiveSavePVersionPanel(bpy.types.Panel):
    bl_label = "Permenant Version"
    bl_idname = "LIVE_SAVE_P_VERSION_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Live Save'

    def draw(self, context):
        layout = self.layout
        addon_prefs = props.preference.prefs()
        myaddonprops = bpy.context.window_manager.my_addon_props
        WindowManager = context.window_manager

        if WindowManager.my_list:
            row = layout.box().column()
            row.template_list("MY_UL_List", "The_List", WindowManager,
                              "my_list", WindowManager, "list_index")
            raw = row.row(align=True)
            raw.operator('my_list.new_item', text='NEW', icon='ADD')
            raw.operator('my_list.delete_item', text='REMOVE', icon='REMOVE')

            item = WindowManager.my_list[WindowManager.list_index]
            row.operator('my_list.open_p_version_index', text="", icon='GREASEPENCIL')
            #row.prop(item, "name")

        bx = layout.box().column()
        sx = bx.grid_flow(align=True)
        sx.operator("livesave.load_pre", text="", icon='REW')
        sx.operator("livesave.load_next", text="", icon='FF')
        bx.operator("live_save.save_p_version", text="Save Permenant Version")
        bx = layout.box().column()
        bx.operator("livesave.load_first", text="First Permenant Version")
        bx.operator("livesave.load_last", text="Last Permenant Version")
        bx.operator("livesave.load_original", text="Load Original File")
        #bx.operator("live_save.open_p_version_folder", text="Open Permenant Version Folder")
        #bx.operator("live_save.delete_p_version", text="Delete Permenant Version")




