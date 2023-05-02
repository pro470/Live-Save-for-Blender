import bpy
import os
import datetime
from .. import props
from .. import utils


class LiveSavePanel(bpy.types.Panel):
    bl_label = "Live Save"
    bl_idname = "LIVE_SAVE_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Live Save'

    def draw(self, context):
        layout = self.layout
        addon_prefs = props.preference.prefs()

        row = layout.row()
        row.prop(addon_prefs, "is_enabled", text="Enable Live Save")

        layout.separator()

        row = layout.row()
        row.prop(addon_prefs, "Timer", text="Timer")

        if addon_prefs.is_enabled:
            layout.operator("wm.live_save_message_handler", text="Start Live Save", emboss=False)
        else:
            layout.operator("wm.live_save_message_handler", text="Stop Live Save", emboss=False)

        layout.separator()
        if bpy.data.is_saved:
            if bpy.data.is_dirty:
                layout.label(text="Edited", icon='ERROR')
            elif os.path.exists(bpy.data.filepath):
                last_save_time = datetime.datetime.fromtimestamp(os.path.getmtime(bpy.data.filepath))
                layout.label(text=f"Saved at {last_save_time:%Y-%m-%d %H:%M:%S}")
        else:
            if utils.comparison.compare_blend_data():
                if os.path.exists(bpy.context.window_manager.my_addon_props.file_path):
                    last_save_time = datetime.datetime.fromtimestamp(os.path.getmtime(bpy.context.window_manager.my_addon_props.file_path))
                    layout.label(text=f"Saved at {last_save_time:%Y-%m-%d %H:%M:%S}")
            else:
                layout.label(text="Edited", icon='ERROR')

        layout.separator()
        layout.operator("wm.save_as_mainfile_with_browser")

