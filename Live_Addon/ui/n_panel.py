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
        myaddonprops = bpy.context.window_manager.my_addon_props

        row = layout.row()
        row.prop(addon_prefs, "is_enabled", text="Enable Live Save")

        layout.separator()

        #only draw when dynamic save is enabled
        if not addon_prefs.dynamic_save:
            row = layout.row()
            row.prop(addon_prefs, "Timer", text="Timer")

            layout.separator()

        row = layout.row()
        row.prop(myaddonprops, "is_enabled_version", text="Enable Version")

        layout.separator()

        #only draw when version is enabled
        if myaddonprops.is_enabled_version:
            row = layout.row()
            row.prop(myaddonprops, "version_count", text="Versions Count")

            layout.separator()

            row = layout.row()
            row.prop(myaddonprops, "version_timer", text="Timer Version")

            layout.separator()

        row = layout.row()
        row.prop(addon_prefs, "background_save", text="Background Save")

        layout.separator()

        row = layout.row()
        row.prop(addon_prefs, "dynamic_save", text="dynamic Save")

        layout.separator()

        layout.operator("wm.save_as_mainfile_with_browser")

        layout.separator()

        layout.operator("live_save.save_p_version", text="Save Permenant Version")

        layout.separator()

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
            if os.path.exists(bpy.context.window_manager.my_addon_props.file_path):
                last_save_time = datetime.datetime.fromtimestamp(os.path.getmtime(bpy.context.window_manager.my_addon_props.file_path))
                layout.label(text=f"Saved at {last_save_time:%Y-%m-%d %H:%M:%S}")
            else:
                layout.label(text="Edited", icon='ERROR')
