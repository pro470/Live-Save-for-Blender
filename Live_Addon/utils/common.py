import bpy
import importlib
from .. import props
"""
props_module1 = props.Live_Addon


# Use props_module.addon here


def module() -> str:
    return props_module1.name


def prefs() -> bpy.types.AddonPreferences:
    return bpy.context.preferences.addons[module()].preferences
    
"""

def file_extension_format():

    addon_prefs = props.preference.prefs()
    image_format = addon_prefs.image_format

    if image_format == 'PNG':
        return '.png'
    elif image_format == 'JPEG':
        return '.jpg'
    elif image_format == 'BMP':
        return '.bmp'
    elif image_format == 'TARGA':
        return '.tga'
    elif image_format == 'OPEN_EXR':
        return '.exr'
    elif image_format == 'HDR':
        return '.hdr'
    elif image_format == 'TIFF':
        return '.tif'
    elif image_format == 'AVI_JPEG':
        return '.avi'
    elif image_format == 'AVI_RAW':
        return '.avi'
    elif image_format == 'FRAMESERVER':
        return '.fs'
    elif image_format == 'Cineon':
        return '.cin'
    elif image_format == 'DPX':
        return '.dpx'
    elif image_format == 'OpenEXR_MULTILAYER':
        return '.exr'
    elif image_format == 'JP2':
        return '.jp2'
    elif image_format == 'IRIS':
        return '.rgb'
    elif image_format == 'J2C':
        return '.j2c'
    elif image_format == 'webp':
        return '.webp'





