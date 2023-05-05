import bpy
from . import preference
from ..utils import file_path



class LiveSavePreferences(bpy.types.AddonPreferences):
    bl_idname = preference.module()

    def update_timer(self, context):
        wm = context.window_manager
        operator = wm.operators.get("wm.live_save_message_handler")
        if operator:
            wm.event_timer_remove(operator.timer)
            operator.timer = wm.event_timer_add(self.Timer, window=context.window)

    def update_live_save(self, context):
        if self.is_enabled:
            bpy.ops.wm.live_save_message_handler('EXEC_DEFAULT')

    Timer: bpy.props.FloatProperty(
        name="Timer",
        description="A slider for the timers",
        default=1.0,
        min=0.0,
        max=10.0,
        soft_min=0.0,
        soft_max=5.0,
        step=1,
        precision=2,
        update=update_timer
    )

    is_enabled: bpy.props.BoolProperty(
        name="Enable Live Save",
        description="Enable or disable Live Save",
        default=True,
        update=update_live_save
    )

    livesavede: bpy.props.StringProperty(
        name='Live Save Directory',
        description='The directory where initial saves will be stored',
        default=file_path.get_default_path(),
        subtype='FILE_PATH'
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "is_enabled")
        layout.prop(self, "Timer")
        layout.prop(self, "livesavede")
