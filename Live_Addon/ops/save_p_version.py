import os
import re
from .. import utils
import bpy
fph = utils.file_path

class save_p_version(bpy.types.Operator):
    bl_idname = 'live_save.save_p_version'
    bl_label = 'Save Previous Version'
    bl_description = 'Save a permenant version of your file'

    blend_match = r"\.blend"
    timestep_regex = r"\d{4}\.\d{2}\.\d{2}_\d{2}-\d{2}-\d{2}"


    def execute(self, context):
        file_path12 = bpy.context.window_manager.my_addon_props.file_path
        matched_blend = re.search(self.blend_match, file_path12)
        if bpy.data.is_saved:
            filepath = bpy.data.filepath
            project_name = os.path.basename(filepath)
            p_version_folder_name = f"{project_name}_permenant_version"
            p_version_folder_path = os.path.join(os.path.dirname(filepath), p_version_folder_name)

            if not os.path.exists(p_version_folder_path):
                os.makedirs(p_version_folder_path, exist_ok=True)

            version_files = sorted([f for f in os.listdir(p_version_folder_path) if f.endswith(".blend")])
            for i in range(len(version_files)):
                if len(version_files) == 0:
                    break
                old_path = os.path.join(p_version_folder_path, version_files[i])
                new_name = f"{project_name}_v{i + 1:03}.blend"
                new_path = os.path.join(p_version_folder_path, new_name)
                os.rename(old_path, new_path)

            version_count = len(os.listdir(p_version_folder_path))

            current_version_name = f"{project_name}_v{version_count + 1:03d}.blend"
            current_version_path = os.path.join(p_version_folder_path, current_version_name)

            bpy.ops.wm.save_as_mainfile(filepath=current_version_path, copy=True)
        elif not os.path.isdir(file_path12) and matched_blend and os.path.exists(file_path12):
            version_folder_path = bpy.context.window_manager.my_addon_props.p_version_path

            if not os.path.exists(version_folder_path):
                bpy.context.window_manager.my_addon_props.p_version_path = fph.build_new_p_file_path_version()
                version_folder_path = bpy.context.window_manager.my_addon_props.p_version_path
                os.makedirs(version_folder_path, exist_ok=True)

            version_files = sorted([f for f in os.listdir(version_folder_path) if f.endswith(".blend")])

            for i in range(len(version_files)):
                if len(version_files) == 0:
                    break
                project_name = version_files[i].split("_v")[0]
                old_path = os.path.join(version_folder_path, version_files[i])
                new_name = f"{project_name}_v{i + 1:03}.blend"
                new_path = os.path.join(version_folder_path, new_name)
                os.rename(old_path, new_path)

            project_name = os.path.basename(version_folder_path)
            project_name = project_name[:-15]

            version_count = len(os.listdir(version_folder_path))
            
            current_version_name = f"{project_name}_v{version_count + 1:03d}.blend"
            current_version_path = os.path.join(version_folder_path, current_version_name)

            bpy.ops.wm.save_as_mainfile(filepath=current_version_path, copy=True)

        return {'FINISHED'}


