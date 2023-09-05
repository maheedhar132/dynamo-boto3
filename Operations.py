from dynamo import *
import sys
import os

database = sys.argv[1]
Operations = sys.argv[2]

for operation in Operations:
    if operation == "createTable":
        dynamo.createtable(database)
    if operation == "addData":
        dynamo.addData(database)