#from dynamo import *
import sys
Operations = sys.argv[1]
print(Operations)
Operations.split(',')
for operation in Operations:
    print(operation)