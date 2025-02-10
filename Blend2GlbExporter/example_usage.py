import subprocess
# -b runs headless, --python will run the script after startup
subprocess.run(["/path/to/blender.exe", "-b", "--python", "/path/to/OverscansLibraryManagementToolPublicScripts/Blend2GlbExporter/raw_script.py"])
