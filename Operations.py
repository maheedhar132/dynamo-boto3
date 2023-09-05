import dynamo
import sys
import os

database = sys.argv[1]
Operations = sys.argv[2]
Operations = Operations.split(",")
for operation in Operations:
    if operation == "createTable":
        print("Creating Table")
        dynamo.createTable(database)
    if operation == "addData":
        print("adding Items")
        dynamo.addData(database)