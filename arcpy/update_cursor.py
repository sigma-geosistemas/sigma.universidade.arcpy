import arcpy

# Create update cursor for feature class 
# 
rows = arcpy.UpdateCursor("D:/St_Johns/data.gdb/roads") 

# Update the field used in buffer so the distance is based on the road 
# type. Road type is either 1, 2, 3 or 4. Distance is in meters. 
# 
for row in rows:
    # Fields from the table can be dynamically accessed from the row object.
    #   Here fields named BUFFER_DISTANCE and ROAD_TYPE are used
    row.BUFFER_DISTANCE = row.ROAD_TYPE * 100
    rows.updateRow(row) 

# Delete cursor and row objects to remove locks on the data 
# 
del row 
del rows