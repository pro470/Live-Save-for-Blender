import bpy
from .. import props
import numpy as np


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

    current_data = {"data": {}}
    for obj in bpy.data.objects:
        obj_data = {}
        for prop_name in dir(obj):
            if not prop_name.startswith("__"):
                try:
                    prop_value = getattr(obj, prop_name)
                    if isinstance(prop_value, (int, float, str, bool)):
                        obj_data[prop_name] = prop_value
                    elif isinstance(prop_value, (tuple, list)):
                        # Convert tuple and list to list before storing in dictionary
                        obj_data[prop_name] = list(prop_value)
                    elif isinstance(prop_value, np.ndarray):
                        # Convert numpy arrays to lists before storing in dictionary
                        obj_data[prop_name] = prop_value.tolist()
                    else:
                        # If the data is not a supported data type, skip it
                        continue
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
                            except:
                                # If there's an error, skip the sub-property
                                pass
                except:
                    # If there's an error, skip the property
                    pass
        current_data["data"][obj.name] = obj_data

    if current_data != stored:
        my_dict['stored_data'] = current_data
        stored = current_data
        # print(stored)
        print(current_data)
        return True
    return False

    # if not np.array_equal(current_data, stored):
