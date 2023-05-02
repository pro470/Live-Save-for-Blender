import bpy
from . import n_panel
from . import menu_label


def register():
    bpy.utils.register_class(n_panel.LiveSavePanel)
    bpy.utils.register_class(menu_label.SaveStatusPanel)
    bpy.types.VIEW3D_MT_editor_menus.append(menu_label.SaveStatusPanel.draw)
    if bpy.app.timers.is_registered(menu_label.redraw_menu):
        bpy.app.timers.register(menu_label.redraw_menu, persistent=True, first_interval=1.0)


def unregister():
    if bpy.app.timers.is_registered(menu_label.redraw_menu):
        bpy.app.timers.unregister(menu_label.redraw_menu)
    bpy.types.VIEW3D_MT_editor_menus.remove(menu_label.SaveStatusPanel.draw)
    bpy.utils.unregister_class(menu_label.SaveStatusPanel)
    bpy.utils.unregister_class(n_panel.LiveSavePanel)


