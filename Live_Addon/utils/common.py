import re

import bpy
import importlib

from .. import props
import os

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


def file_path_test(number):
    new_filepath = new_file_path_func(number)

    # check if the new filepath exists
    if os.path.exists(new_filepath):
        print(f"{new_filepath} already exists!")
        return True
    else:
        print(f"{new_filepath} does not exist.")
        return False


def new_file_path_func(number):
    new_filepath = "Bernd"
    addon_prefs = props.preference.prefs()
    print(bpy.context.window_manager.my_addon_props.p_version_path)

    if bpy.data.is_saved or os.path.exists(bpy.context.window_manager.my_addon_props.p_version_path):
        file_path = bpy.data.filepath
        dirname = os.path.dirname(file_path)
        matched = re.search(r"_permenant_version", file_path)

        if matched:
            target_folder = os.path.dirname(file_path)
            # Get a list of all .blend files in the target folder
            blend_files = [f for f in os.listdir(target_folder) if f.endswith(".blend")]

            # Sort the blend files by their creation time, with the oldest file first
            oldest_first = sorted(blend_files, key=lambda f: os.path.getctime(os.path.join(target_folder, f)))

            # Extract just the filenames from the file paths
            oldest_first_filenames = [os.path.basename(f) for f in oldest_first]

            filename = os.path.basename(file_path)

            try:
                if isinstance(number, int):
                    target_file_index = oldest_first_filenames.index(filename)
                    print(f"The index of {file_path} is {target_file_index}")
                    new_filepath = os.path.join(dirname, oldest_first[target_file_index + number])
                elif isinstance(number, str):
                    if number == "first":
                        new_filepath = os.path.join(dirname, oldest_first[0])
                    elif number == "last":
                        new_filepath = os.path.join(dirname, oldest_first[-1])
            except ValueError and IndexError:
                print(f"{file_path} is not in the list")

            return new_filepath

        else:
            project_name = os.path.splitext(os.path.basename(file_path))[0]
            dirname = os.path.dirname(file_path)
            p_version_folder_name = f"{project_name}_permenant_version"
            p_version_folder_path = os.path.join(dirname, p_version_folder_name)
            print(p_version_folder_path)
            target_folder = p_version_folder_path

            if os.path.exists(target_folder):
                # get the directory and filename without extension
                directory, filename = os.path.split(file_path)
                filename, ext = os.path.splitext(filename)

                # if not, start with version 1
                new_version = number
                new_filename = f"{filename}_v{new_version:03}{ext}"

                # create the new filepath with the new filename
                new_filepath = os.path.join(target_folder, new_filename)
                return new_filepath

    elif os.path.exists(bpy.context.window_manager.my_addon_props.p_version_path):
        target_folder = bpy.context.window_manager.my_addon_props.p_version_path
        new_version = number
        # loop through all blend files in the directory and find the matching filepath
        version_files = sorted([f for f in os.listdir(target_folder) if f.endswith(".blend")])
        new_filepath = os.path.join(target_folder, version_files[0])
        return new_filepath

    return new_filepath


def file_path_version_open(number):
    new_filepath = new_file_path_func(number)
    # check if the new filepath exists
    if os.path.exists(new_filepath):
        bpy.ops.wm.open_mainfile(filepath=new_filepath)
