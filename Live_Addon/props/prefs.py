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
            bpy.ops.wm.user_action_detector('EXEC_DEFAULT')

    Timer: bpy.props.FloatProperty(
        name="Timer",
        description="A slider for the timers",
        default=1.0,
        min=0.1,
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

    background_save: bpy.props.BoolProperty(
        name="Background Save",
        description="Enable or disable Background Save(when on data lost can happen)",
        default=False,
    )

    dynamic_save: bpy.props.BoolProperty(
        name="Dynamic Save",
        description="Enable or disable Dynamic Save",
        default=True,
    )

    image_format: bpy.props.EnumProperty(
        name="Image Format",
        description="Image Format",
        items=[
            ('PNG', 'PNG', ' save images with the PNG format'),
            ('JPEG', 'JPEG', 'save images with the JPEG format'),
            ('BMP', 'BMP', 'save images with the BMP format'),
            ('TARGA', 'TARGA', 'save images with the TARGA format'),
            ('OPEN_EXR', 'OPEN_EXR', 'save images with the OPEN_EXR format'),
            ('HDR', 'HDR', 'save images with the HDR format'),
            ('TIFF', 'TIFF', 'save images with the TIFF format'),
            ('AVI_JPEG', 'AVI_JPEG', 'save images with the AVI_JPEG format'),
            ('AVI_RAW', 'AVI_RAW', 'save images with the AVI_RAW format'),
            ('FRAMESERVER', 'FRAMESERVER', 'save images with the FRAMESERVER format'),
            ('Cineon', 'Cineon', 'save images with the Cineon format'),
            ('DPX', 'DPX', 'save images with the DPX format'),
            ('OpenEXR_MULTILAYER', 'OpenEXR_MULTILAYER', 'save images with the OpenEXR_MULTILAYER format'),
            ('JP2', 'JP2', 'save images with the JP2 format'),
            ('IRIS', 'IRIS', 'save images with the IRIS format'),
            ('J2C', 'J2C', 'save images with the J2C format'),
            ('webp', 'webp', 'save images with the webp format')
        ],
        default='PNG',
    )

    image_file_path: bpy.props.StringProperty(
        name='Image File Path',
        description='The directory where initial saves will be stored',
        default=file_path.get_default_path(),
        subtype='FILE_PATH'
    )

    auto_start_save: bpy.props.BoolProperty(
        name="Auto Start Save",
        description="Enable or disable Auto Start Save",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "is_enabled")
        layout.prop(self, "Timer")
        layout.prop(self, "livesavede")
        layout.prop(self, "background_save")
        layout.prop(self, "dynamic_save")
        layout.prop(self, "image_format")
        layout.prop(self, "image_file_path")
        layout.prop(self, "auto_start_save")
