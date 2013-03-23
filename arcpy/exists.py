import arcpy
from arcpy import env

# Set the current workspace
# 
env.workspace = "C:/Data/MyData.gdb"

# Check for existance of the output data before running the Buffer tool.
# 
if arcpy.Exists("RoadsBuff"):
    arcpy.Delete_management("RoadsBuff")

try:
    arcpy.Buffer_analysis("Roads", "RoadsBuff", "100 meters")
    arcpy.AddMessage("Buffer complete")
except:
    arcpy.AddError(arcpy.GetMessages(2))