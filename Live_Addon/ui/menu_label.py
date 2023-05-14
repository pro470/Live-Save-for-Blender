import bpy
import os
import time


class SaveStatusPanel(bpy.types.Operator):
    bl_idname = "wm.save_status_panel"
    bl_label = "Save Status"


    def draw(self, context):
        layout = self.layout

        # check if file is dirty
        if bpy.data.is_dirty:
            row = layout.row(align=True)
            row.label(text="Edited", icon='ERROR')
        else:
            row = layout.row(align=True)
            row.label(text="", icon='NONE')

    def modal(self, context, event):
        if event.type in {'ESC'}:
            wm = context.window_manager
            wm.event_timer_remove(self._timer)
            wm.modal_handler_remove(self)
            return {'CANCELLED'}
        elif event.type == 'TIMER':
            if bpy.data.is_dirty:
                self.tag_redraw()
            else:
                self.tag_redraw()
        return {'PASS_THROUGH'}


def redraw_menu():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'UI':
                    region.tag_redraw()
    return 0.1

