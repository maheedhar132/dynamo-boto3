from dynamo import *
import sys
import os

database = sys.argv[1]
Operations = sys.argv[2]
print(Operations)
print(type(Operations))
Operations=Operations.split(",")
for operation in Operations:
    dynamo.operation(database)