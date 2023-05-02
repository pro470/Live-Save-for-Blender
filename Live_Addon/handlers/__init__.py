import bpy
from . import live_load_hanlder
from . import live_save_handler
from . import undo_redo


def register():
    if live_load_hanlder.auto_start not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(live_load_hanlder.auto_start)

    if live_save_handler.on_save_post_handler not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(live_save_handler.on_save_post_handler)


def unregister():
    if live_load_hanlder.auto_start in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(live_load_hanlder.auto_start)

    if live_save_handler.on_save_post_handler in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(live_save_handler.on_save_post_handler)