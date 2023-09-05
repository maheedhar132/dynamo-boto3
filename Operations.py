#from dynamo import *
import sys
Operations = sys.argv[1]
print(Operations)
print(type(Operations))
Operations=Operations.split(",")
for operation in Operations:
    print(operation)