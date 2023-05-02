bl_info = {
    "name": "Live Save 2",
    "description": "Automatically saves the project with a timestamp when changes are made",
    "author": "Your Name",
    "version": (0, 1),
    "blender": (3, 3, 0),
    "location": "View3D > UI panel",
    "warning": "",
    "category": "System"
}


from . import Live_Addon


def register():
    Live_Addon.register()


def unregister():
    Live_Addon.unregister()
