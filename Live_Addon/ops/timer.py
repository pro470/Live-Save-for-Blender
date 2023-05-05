import threading

import bpy
from .. import utils
import importlib

props_module = importlib.import_module("Live Save.Live_Addon.props.preference")
from .. import handlers
# Use props_module.addon here

class LiveSaveMessageHandler(bpy.types.Operator):
    bl_idname = "wm.live_save_message_handler"
    bl_label = "Live Save Message Handler"

    _timer = None
    is_running = False
    is_other_script: bpy.props.BoolProperty(default=False)
    onlyonce: bpy.props.BoolProperty(default=False)

    def update_timer(self, context):
        addon_prefs = props_module.prefs()
        wm = context.window_manager
        if self._timer != addon_prefs.Timer:
            wm.event_timer_remove(self._timer)
            self._timer = None
        if not self._timer:
            self._timer = wm.event_timer_add(addon_prefs.Timer, window=context.window)

    def modal(self, context, event):
        if event.type == 'TIMER':
            addon_prefs = props_module.prefs()
            if not addon_prefs.is_enabled:
                self.cancel(context)
                return {'CANCELLED'}
            self.update_timer(context)
            if utils.comparison.check_undo_redo(context):
                print("i was called")
                self.properties.is_other_script = True
            if bpy.data.is_dirty or self.is_other_script:
                if not self.is_running:
                    self.is_running = True
                    threading.Thread(target=self.my_thread_function).start()
        return {'PASS_THROUGH'}

    def execute(self, context):
        addon_prefs = props_module.prefs()
        wm = context.window_manager
        self._timer = wm.event_timer_add(addon_prefs.Timer, window=context.window)
        wm.modal_handler_add(self)
        bpy.app.handlers.undo_post.append(handlers.undo_redo.redo_handler)
        bpy.app.handlers.redo_post.append(handlers.undo_redo.redo_handler)
        bpy.ops.wm.user_action_detector('EXEC_DEFAULT')

        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        bpy.app.handlers.undo_post.remove(handlers.undo_redo.redo_handler)
        bpy.app.handlers.redo_post.remove(handlers.undo_redo.redo_handler)

        return {'CANCELLED'}

    def my_thread_function(self):
        utils.saving_function.save_blend_file()
        utils.saving_function.save_image_textures()
        utils.saving_function.save_image_udim_textures()
        self.properties.is_other_script = False
        self.is_running = False

    @property
    def timer(self):
        return self._timer
