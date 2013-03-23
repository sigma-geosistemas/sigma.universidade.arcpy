import arcpy
from arcpy import env

# Set the workspace environment setting
#
env.workspace = "c:/St_Johns/data.gdb"

# Set the XYTolerance environment setting
#
env.XYTolerance = 2.5

# Calculate the default spatial grid index, divide in half, then
#   set the spatial grid 1 environment setting
#
result = arcpy.CalculateDefaultGridIndex_management("roads")

env.spatialGrid1 = float(result.getOutput(0)) / 2

# Clip the roads by the urban area feature class
#
arcpy.Clip_analysis("roads","urban_area","urban_roads")