import dynamoDB
import sys
import os

database = sys.argv[1]
Operations = sys.argv[2]
Operations = Operations.split(",")
for operation in Operations:
    if operation == "createTable":
        print("Creating Table")
        create = dynamoDB.createTable(database)
        print(create)
        tableData = dynamoDB.readTable(database)
        print(tableData)
    if operation == "addData":
        print("adding Items")
        addstatus = dynamoDB.addData(database)
        print(addstatus)
        tableData = dynamoDB.readTable(database)
        print(tableData)
    if operation == "updateItems":
        print("updating Items...")
        updateStatus = dynamoDB.updateItems(database)
        print(updateStatus)
    if operation == "getItem":
        print("getting data")
        getStatus = dynamoDB.getItem(database)
        print(getStatus)
    if operation == "deleteData":
        print("Deleting requested Data")
        deleteStatus = dynamoDB.deleteData(database)
        print(deleteStatus)