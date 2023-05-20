import bpy
import os
import datetime
from .. import props
from .. import utils


class LiveSaveVersionPanel(bpy.types.Panel):
    bl_label = "Version"
    bl_idname = "LIVE_SAVE_VERSION_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Live Save'

    def draw(self, context):
        layout = self.layout
        props.preference.prefs()
        myaddonprops = bpy.context.window_manager.my_addon_props

        bx = layout.box().column()
        bx.prop(myaddonprops, "is_enabled_version", text="Enable Version")
        col = bx.column()
        col.enabled = myaddonprops.is_enabled_version
        col.prop(myaddonprops, "version_count", text="Versions Count")
        col.prop(myaddonprops, "version_timer", text="Timer Version")

