import arcpy

# Create insert cursor for table 
# 
rows = arcpy.InsertCursor("D:/St_Johns/data.gdb/roads_lut") 
x = 1 

# Create 25 new rows. Set the initial row ID and distance values 
# 
while x <= 25: 
    row = rows.newRow() 
    row.rowid = x 
    row.distance = 100
    rows.insertRow(row) 
    x += 1

# Delete cursor and row objects to remove locks on the data 
# 
del row 
del rows