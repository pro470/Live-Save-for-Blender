import bpy

name = __name__.partition(".")[0]


class LiveSaveProps(bpy.types.PropertyGroup):
    addon: bpy.props.StringProperty(
        name='Live_Addon',
        description='Live module',
        default=name,
    )

    @property
    def prefs(self) -> bpy.types.AddonPreferences:
        from .. import props

        return props.preference.prefs()
