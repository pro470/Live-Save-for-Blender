import os
import bpy
import platform
import datetime
import re
import tempfile
from .. import props


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


# file_name = "live_backup"
# current_time = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
# file_path = os.path.join(appdata_folder, file_name + current_time + ".blend")



