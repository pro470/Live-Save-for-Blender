import bpy
import os
import shutil


def save_version():
    # Get the current Blender file path
    filepath = bpy.data.filepath

    # Extract the project name without the file extension
    project_name = os.path.splitext(os.path.basename(filepath))[0]

    # Create the version folder name with the project name and version count
    version_folder_name = f"{project_name}_version_folder"

    # Create the full path for the version folder
    version_folder_path = os.path.join(os.path.dirname(filepath), version_folder_name)

    # Create the version folder if it doesn't exist
    if not os.path.exists(version_folder_path):
        os.mkdir(version_folder_path)

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
        old_path = os.path.join(version_folder_path, version_files_new[i])
        new_name = f"{project_name}_v{i + 1:03}.blend"
        new_path = os.path.join(version_folder_path, new_name)
        os.rename(old_path, new_path)

    version_count = len(os.listdir(version_folder_path))

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
        bpy.app.timers.register(save_version)
    else:
        bpy.app.timers.unregister(save_version)
