import bpy


def redo_handler(dummy):
    print("undo did happend")
    bpy.context.window_manager.my_addon_props.exec_count += 1
