# Importing arcpy
#
import arcpy

# Set the workspace environment and run Clip_analysis
arcpy.env.workspace = "C:/Data/Tongass"
arcpy.Clip_analysis("standb4", "clipcov", "standby_clip", "1.25")