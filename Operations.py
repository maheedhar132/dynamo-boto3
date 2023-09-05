from dynamo import *
import sys
import os

database = sys.argv[1]
Operations = sys.argv[2]

for operation in Operations:
    if operation == "createTable":
        print("Creating Table")
        dynamo.createtable(database)
    if operation == "addData":
        print("adding Items")
        dynamo.addData(database)