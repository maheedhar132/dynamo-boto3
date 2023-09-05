#from dynamo import *
import sys
Operations = sys.argv[1]
Operations.split(',')
for operation in Operations:
    print(operation)