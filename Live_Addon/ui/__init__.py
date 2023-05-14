import bpy
from . import n_panel
from . import menu_label
from . import p_version_n_panel
from . import version_n_panel


def register():
    bpy.utils.register_class(n_panel.LiveSavePanel)
    bpy.utils.register_class(menu_label.SaveStatusPanel)
    bpy.utils.register_class(p_version_n_panel.LiveSavePVersionPanel)
    bpy.utils.register_class(version_n_panel.LiveSaveVersionPanel)
    bpy.types.VIEW3D_MT_editor_menus.append(menu_label.SaveStatusPanel.draw)
    if bpy.app.timers.is_registered(menu_label.redraw_menu):
        bpy.app.timers.register(menu_label.redraw_menu, persistent=True, first_interval=1.0)


def unregister():
    if bpy.app.timers.is_registered(menu_label.redraw_menu):
        bpy.app.timers.unregister(menu_label.redraw_menu)
    bpy.types.VIEW3D_MT_editor_menus.remove(menu_label.SaveStatusPanel.draw)
    bpy.utils.unregister_class(menu_label.SaveStatusPanel)
    bpy.utils.unregister_class(n_panel.LiveSavePanel)
    bpy.utils.unregister_class(p_version_n_panel.LiveSavePVersionPanel)
    bpy.utils.unregister_class(version_n_panel.LiveSaveVersionPanel)


