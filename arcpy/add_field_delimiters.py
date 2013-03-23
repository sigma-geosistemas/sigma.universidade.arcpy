import arcpy
from arcpy import env

fieldName      = arcpy.GetParameterAsText(0)
wkspace        = arcpy.GetParameterAsText(1)
in_features    = arcpy.GetParameterAsText(2)
out_feat_class = arcpy.GetParameterAsText(3)
stateVal       = arcpy.GetParameterAstext(4)

# AddFieldDelimiters will return a field name with the proper
#  field delimiters for the workspace specified.
#
newName = arcpy.AddFieldDelimiters("C:/Data", fieldName)

# Use delimited field for Select tool SQL expression
#
sqlExp = newName + " = " + stateVal
env.workspace = wkspace
arcpy.Select_analysis(in_features, out_feat_class, sqlExp)   