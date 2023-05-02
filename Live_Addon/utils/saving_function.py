import bpy
import os
import datetime
from . import file_path
from . import comparison
import importlib

props_module = importlib.import_module("Live Save.Live_Addon.props.preference")

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
                    documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
                    images_dir = os.path.join(documents_dir, "Images from Blender")
                    os.makedirs(images_dir, exist_ok=True)
                    current_time_images2 = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
                    img.filepath = os.path.join(images_dir, img.name + current_time_images2 + ".png")
                    img.save()
        except Exception as e:
            print(str(e))


def save_image_udim_textures():
    for img in bpy.data.images:
        try:
            if img.is_dirty:
                if not img.filepath:
                    documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
                    current_time_images1 = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
                    images_dir = os.path.join(documents_dir, "Images from Blender")
                    os.makedirs(images_dir, exist_ok=True)
                    udim = '<UDIM>'
                    img.filepath = os.path.join(images_dir, img.name + current_time_images1 + udim + ".png")
                    img.save()
        except Exception as e:
            print(str(e))


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
        else:
            bpy.context.window_manager.my_addon_props.file_path = fph.create_new_file_path()
            print("wrong place")
            save_to_file(bpy.context.window_manager.my_addon_props.file_path)
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
