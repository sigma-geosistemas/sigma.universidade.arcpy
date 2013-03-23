import arcpy

# Abra um search cursor
# dados de uberlandia
rows = arcpy.SearchCursor("C:/uber.gdb/urbano/quadras_poligono", "", "", "NAME; STATE_NAME; POP2000", 
                          "STATE_NAME A; POP2000 D") 
currentState = "" 

# Iterate through the rows in the cursor 
# 
for row in rows: 
    if currentState != row.STATE_NAME: 
        currentState = row.STATE_NAME 

    # Print out the state name, county, and population 
    # 
    print "State: %s, County: %s, population: %i" % \
            (row.STATE_NAME, row.NAME, row.POP2000) 