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
        dynamoDB.readTable(database)
    if operation == "addData":
        print("adding Items")
        dynamoDB.addData(database)