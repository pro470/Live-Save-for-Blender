import importlib
import bpy

props_module = importlib.import_module("Live Save.Live_Addon.props.preference")



class UserActionDetector(bpy.types.Operator):
    bl_idname = "wm.user_action_detector"
    bl_label = "User Action Detector"

    def modal(self, context, event):
        if event.type in {'LEFTMOUSE', 'RIGHTMOUSE'} and event.value == 'RELEASE':
            print("User action detected")
            bpy.context.window_manager.my_addon_props.mouse_detect = True
            addon_prefs = props_module.prefs()
            if not addon_prefs.is_enabled:
                self.cancel(context)
                return {'CANCELLED'}

        return {'PASS_THROUGH'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
