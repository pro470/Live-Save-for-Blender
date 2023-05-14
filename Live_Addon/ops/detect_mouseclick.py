import importlib
import bpy
from .. import props

props_module = props.preference


class UserActionDetector(bpy.types.Operator):
    bl_idname = "wm.user_action_detector"
    bl_label = "User Action Detector"

    def modal(self, context, event):
        #i want to add the enter key to the list of keys that will trigger the operator
        if event.type in {'LEFTMOUSE', 'RIGHTMOUSE', 'RET'} and event.value == 'RELEASE':
            print("User action detected")
            bpy.context.window_manager.my_addon_props.mouse_detect = True
            addon_prefs = props_module.prefs()
            if not addon_prefs.is_enabled:
                self.cancel(context)
                return {'CANCELLED'}

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        return {'CANCELLED'}
