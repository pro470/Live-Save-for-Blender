import os
import bpy
import platform
import datetime
import re
import tempfile
from .. import props
from . import common


def get_default_path():
    if platform.system() == "Windows":
        appdata_folder = os.path.join(os.environ["APPDATA"])
    else:
        appdata_folder = os.path.join(os.environ["HOME"], ".config")
    return appdata_folder


def build_new_file_path():
    current_time = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
    timestep_regex = r"\d{4}\.\d{2}\.\d{2}_\d{2}-\d{2}-\d{2}"
    new_path = re.sub(timestep_regex, current_time, bpy.context.window_manager.my_addon_props.file_path)
    return new_path


def match_in_timestep():
    if os.path.exists(bpy.context.window_manager.my_addon_props.file_path):
        timestep_regex = r"\d{4}\.\d{2}\.\d{2}_\d{2}-\d{2}-\d{2}"
        matched1 = re.search(timestep_regex, bpy.context.window_manager.my_addon_props.file_path)
        return matched1
    else:
        return False


def create_new_file_path():
    file_name = "my_blend_file_"
    current_time = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
    addonpref = props.preference.prefs()
    created_filepath = os.path.join(addonpref.livesavede, file_name + current_time + ".blend")
    return created_filepath


def create_new_file_path_version():
    project_name = os.path.splitext(os.path.basename(bpy.context.window_manager.my_addon_props.file_path))[0]

    # Create the version folder name with the project name and version count
    version_folder_name = f"{project_name}_version_folder"

    # Create the full path for the version folder
    version_folder_path = os.path.join(os.path.dirname(bpy.context.window_manager.my_addon_props.file_path),
                                       version_folder_name)

    return version_folder_path


def build_new_p_file_path_version():
    file_name = "my_blend_file_"
    current_time = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
    addonpref = props.preference.prefs()
    created_filepath = os.path.join(addonpref.livesavede, file_name + current_time)
    version_folder_name = f"{created_filepath}_permenant_version_folder"
    version_folder_path = os.path.join(os.path.dirname(bpy.context.window_manager.my_addon_props.file_path),
                                       version_folder_name)
    return version_folder_path


def make_image_dir():
    addonpref = props.preference.prefs()
    image_dir = os.path.join(addonpref.image_file_path, "Images from Blender")
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)
    return image_dir


def make_image_file_path_udim(image_name):
        image_dir = make_image_dir()
        currrent_time = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
        udim = '<UDIM>'
        image_file_path = os.path.join(image_dir, image_name + currrent_time + udim + common.file_extension_format())
        return image_file_path


def make_image_file_path(image_name):
        image_dir = make_image_dir()
        currrent_time = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
        image_file_path = os.path.join(image_dir, image_name + currrent_time + common.file_extension_format())
        return image_file_path

# file_name = "live_backup"
# current_time = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
# file_path = os.path.join(appdata_folder, file_name + current_time + ".blend")
