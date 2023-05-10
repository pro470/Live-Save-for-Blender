import re

import bpy
import os
import shutil
from .. import utils
from .. import props
prefs = props.preference.prefs()


def save_version():
    file_path12 = bpy.context.window_manager.my_addon_props.file_path
    blend_match = r"\.blend"
    timestep_regex = r"\d{4}\.\d{2}\.\d{2}_\d{2}-\d{2}-\d{2}"
    matched_blend = re.search(blend_match, file_path12)
    # Get the current Blender file path
    if bpy.data.is_saved and bpy.data.is_dirty:
        filepath = bpy.data.filepath

        # Extract the project name without the file extension
        project_name = os.path.splitext(os.path.basename(filepath))[0]

        # Create the version folder name with the project name and version count
        version_folder_name = f"{project_name}_version_folder"

        # Create the full path for the version folder
        version_folder_path = os.path.join(os.path.dirname(filepath), version_folder_name)

        # Create the version folder if it doesn't exist
        if not os.path.exists(version_folder_path):
            os.makedirs(version_folder_path, exist_ok=True)

    elif not os.path.isdir(file_path12) and matched_blend and os.path.exists(file_path12) and utils.comparison.compare_blend_data():

        version_folder_path = bpy.context.window_manager.my_addon_props.file_path_version
        # Extract name without the .blender extension but not with os.path.splitext
        #project_name = os.path.basename(version_folder_path)
        #create project name without the .blend extension
        #project_name = project_name[:-15]

        # Create the version folder if it doesn't exist
        if not os.path.exists(version_folder_path):
            os.makedirs(version_folder_path, exist_ok=True)
    else:
        return bpy.context.window_manager.my_addon_props.version_timer

    # get existing version files and sort by name
    version_files = sorted([f for f in os.listdir(version_folder_path) if f.endswith(".blend")])

    # Delete the oldest version(s) if there are more than three versions
    if len(version_files) >= bpy.context.window_manager.my_addon_props.version_count:
        # delete the oldest version files until bpy.context.window_manager.my_addon_props.version_count is reached
        for i in range(len(version_files) - bpy.context.window_manager.my_addon_props.version_count + 1):
            os.remove(os.path.join(version_folder_path, version_files[i]))
    version_files_new = sorted([f for f in os.listdir(version_folder_path) if f.endswith(".blend")])
        # rename existing version files to ensure unique names
    for i in range(len(version_files_new)):
        if len(version_files_new) == 0:
            break
        elif re.search(timestep_regex, version_files_new[i]):
            project_name = version_files_new[i].split("_v")[0]
        old_path = os.path.join(version_folder_path, version_files_new[i])
        new_name = f"{project_name}_v{i + 1:03}.blend"
        new_path = os.path.join(version_folder_path, new_name)
        os.rename(old_path, new_path)

    version_count = len(os.listdir(version_folder_path))
    if re.search(timestep_regex, version_folder_path):
        # Extract name without the .blender extension but not with os.path.splitext
        project_name = os.path.basename(version_folder_path)
        #create project name without the .blend extension
        project_name = project_name[:-15]

    # Save the current version with a unique file name
    current_version_name = f"{project_name}_v{version_count + 1:03d}.blend"
    current_version_path = os.path.join(version_folder_path, current_version_name)

    bpy.ops.wm.save_as_mainfile(filepath=current_version_path, copy=True)

    return bpy.context.window_manager.my_addon_props.version_timer


def update_version_timer(self, context):
    if bpy.app.timers.is_registered(save_version):
        bpy.app.timers.unregister(save_version)
        bpy.app.timers.register(save_version)



def update_version_bool(self, context):
    if self.is_enabled_version:
        if not bpy.app.timers.is_registered(save_version):
            bpy.app.timers.register(save_version)
    else:
        if bpy.app.timers.is_registered(save_version):
            bpy.app.timers.unregister(save_version)
