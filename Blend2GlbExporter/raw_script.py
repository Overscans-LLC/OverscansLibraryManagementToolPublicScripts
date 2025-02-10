import bpy

# path to this python file that is filled in with values below so this can be passed into blender
py_file = {py_file}
# path to the blender file we want to load
filepath = {blend_path}
# name of the object you want to export as a glb in the blender file
object_name = {obj_name}
# full path of the .glb file you're exporting from the blender file
output_glb = {output_glb}
try:
    bpy.ops.wm.open_mainfile(filepath=filepath)
    bpy.ops.object.select_all(action='DESELECT')
    obj = bpy.data.objects.get(object_name)
    if obj:
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.export_scene.gltf(filepath=output_glb, check_existing=True, use_selection=True)
    # This can be ignored if you don't want to check the python file after this runs 
    # to communicate back a failure to the process that launching blender with this py file
    else:
        with open(py_file, \"w\") as file_opened:
            desktop_ini_contents = file_opened.write('failure')
except:
    # This can be ignored if you don't want to check the python file after this runs 
    # to communicate back a failure to the process that launching blender with this py file
    with open(py_file, \"w\") as file_opened:
        desktop_ini_contents = file_opened.write('failure')

# Quit blender
bpy.ops.wm.quit_blender()
