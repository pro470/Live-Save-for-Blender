import bpy
from .. import props
import numpy as np
import sqlite3


def check_undo_redo(context):
    print("i called ")
    wm = context.window_manager
    current_count = bpy.context.window_manager.my_addon_props.exec_count
    print("current exec")
    print(current_count)
    previous_count = wm.get("_previous_count", 0)
    if current_count != previous_count:
        print("ungleich")
        wm["_previous_count"] = current_count
        print("setting current")
        return True
    return False


my_dict = {}
stored = my_dict.get("stored_data", {})


def compare_blend_data():
    global stored
    if bpy.context.window_manager.my_addon_props.mouse_detect:
        
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
            *bpy.data.texts,
            *bpy.data.volumes,
            *bpy.data.pointclouds,
            *bpy.data.movieclips,
            *bpy.data.lightprobes,
            *bpy.data.lattices,
            *bpy.data.hair_curves,
            *bpy.data.cache_files,
            *bpy.data.linestyles,
            *bpy.data.speakers
        }

        current_data = {"data": {}}
        for obj in data_blocks:
            obj_data = {}
            for prop_name in dir(obj):
                if prop_name:
                    try:
                        prop_value = getattr(obj, prop_name)
                        if not prop_name.startswith("__"):
                            obj_data[prop_name] = prop_value

                        for sub_prop_name in dir(prop_value):
                            if not sub_prop_name.startswith("__"):
                                try:
                                    sub_prop_value = getattr(prop_value, sub_prop_name)
                                    if isinstance(sub_prop_value, (int, float, str, bool)):
                                        obj_data[f"{prop_name}.{sub_prop_name}"] = sub_prop_value
                                    elif isinstance(sub_prop_value, (tuple, list)):
                                        # Convert tuple and list to list before storing in dictionary
                                        obj_data[f"{prop_name}.{sub_prop_name}"] = list(sub_prop_value)
                                    elif isinstance(sub_prop_value, np.ndarray):
                                        # Convert numpy arrays to lists before storing in dictionary
                                        obj_data[f"{prop_name}.{sub_prop_name}"] = sub_prop_value.tolist()
                                    else:
                                        # If the sub-property is not a supported data type, skip it
                                        continue
                                    for sub_sub_prop_name in dir(sub_prop_value):
                                        if not sub_sub_prop_name.startswith("__"):
                                            try:
                                                sub_sub_prop_value = getattr(sub_prop_value, sub_sub_prop_name)
                                                if isinstance(sub_sub_prop_value, (int, float, str, bool)):
                                                    obj_data[f"{prop_name}.{sub_prop_name}.{sub_sub_prop_name}"] = sub_sub_prop_value
                                                elif isinstance(sub_sub_prop_value, (tuple, list)):
                                                    # Convert tuple and list to list before storing in dictionary
                                                    obj_data[f"{prop_name}.{sub_prop_name}.{sub_sub_prop_name}"] = list(sub_sub_prop_value)
                                                elif isinstance(sub_sub_prop_value, np.ndarray):
                                                    # Convert numpy arrays to lists before storing in dictionary
                                                    obj_data[f"{prop_name}.{sub_prop_name}.{sub_sub_prop_name}"] = sub_sub_prop_value.tolist()
                                                else:
                                                    # If the sub-sub-property is not a supported data type, skip it
                                                    continue
                                            except:
                                                # If there's an error, skip the sub-sub-property
                                                pass
                                except:
                                    # If there's an error, skip the sub-property
                                    pass
                    except:
                        # If there's an error, skip the property
                        pass
            current_data["data"][obj] = obj_data

        if current_data != stored:
            my_dict['stored_data'] = current_data
            stored = current_data
            # print(stored)
            # print(current_data)
            print("made it here")
            bpy.context.window_manager.my_addon_props.mouse_detect = False
            return True
        bpy.context.window_manager.my_addon_props.mouse_detect = False
    return False

    # if not np.array_equal(current_data, stored):
