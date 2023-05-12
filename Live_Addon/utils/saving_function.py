import bpy
import os
import datetime
from . import file_path
from . import comparison
from . import common
import importlib


fph = file_path


def run_once():
    has_run = False

    def inner():
        nonlocal has_run
        if not has_run:
            print("This function will only execute once.")
            has_run = True
            return True
        else:
            return False

    return inner


def save_to_file(file_path1):
    bpy.ops.wm.save_as_mainfile(filepath=file_path1, copy=True)


def save_image_textures():
    for img in bpy.data.images:
        try:
            if img.is_dirty:
                if img.filepath:
                    img.save()
                else:
                    img.filepath = file_path.make_image_file_path(img.name)
                    img.save()
        except Exception as e:
            print(str(e))
            if not os.path.exists(img.filepath):
                img.filepath = file_path.make_image_file_path_udim(img.name)
                img.save()


def save_blend_file():

    if bpy.data.is_saved:
        bpy.ops.wm.save_mainfile()
    elif comparison.compare_blend_data():
        if fph.match_in_timestep():
            new_file_path = fph.build_new_file_path()
            print("im about to delete")
            print(bpy.context.window_manager.my_addon_props.file_path, new_file_path)
            os.rename(bpy.context.window_manager.my_addon_props.file_path, new_file_path)
            print("i deleted")
            bpy.context.window_manager.my_addon_props.file_path = new_file_path
            if os.path.exists(bpy.context.window_manager.my_addon_props.file_path_version):
                new_version_folder = fph.create_new_file_path_version()
                os.rename(bpy.context.window_manager.my_addon_props.file_path_version, new_version_folder)
                bpy.context.window_manager.my_addon_props.file_path_version = new_version_folder
            elif bpy.context.window_manager.my_addon_props.is_enabled_version:
                new_version_folder = fph.create_new_file_path_version()
                bpy.context.window_manager.my_addon_props.file_path_version = new_version_folder
        else:
            bpy.context.window_manager.my_addon_props.file_path = fph.create_new_file_path()
            print("wrong place")
            save_to_file(bpy.context.window_manager.my_addon_props.file_path)
            if bpy.context.window_manager.my_addon_props.is_enabled_version:
                new_version_folder = fph.create_new_file_path_version()
                bpy.context.window_manager.my_addon_props.file_path_version = new_version_folder
        # write all materials, textures and node groups to a library
        data_blocks = {
            *bpy.data.meshes,
            *bpy.data.materials,
            *bpy.data.textures,
            *bpy.data.images,
            *bpy.data.objects,
            *bpy.data.lights,
            *bpy.data.cameras,
            *bpy.data.curves,
            *bpy.data.armatures,
            *bpy.data.actions,
            *bpy.data.libraries,
            *bpy.data.scenes,
            *bpy.data.sounds,
            *bpy.data.worlds,
            *bpy.data.fonts,
            *bpy.data.grease_pencils,
            *bpy.data.metaballs,
            *bpy.data.paint_curves,
            *bpy.data.particles,
            *bpy.data.shape_keys,
            *bpy.data.speakers,
            *bpy.data.texts,
            *bpy.data.window_managers,
            *bpy.data.workspaces,
            *bpy.data.volumes,
            *bpy.data.pointclouds,
            *bpy.data.movieclips,
            *bpy.data.lightprobes,
            *bpy.data.libraries,
            *bpy.data.lattices,
            *bpy.data.hair_curves,
            *bpy.data.collections,
            *bpy.data.cache_files,
            *bpy.data.linestyles,
            *bpy.data.brushes,
            *bpy.data.speakers,
            *bpy.data.screens
        }
        bpy.data.libraries.write(bpy.context.window_manager.my_addon_props.file_path, data_blocks)
        print("Data appended successfully to the copied blend file.")
    else:
        pass
