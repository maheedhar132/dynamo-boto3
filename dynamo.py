import boto3
import json
import pathlib
import botocore
import yaml

with open("path.yaml", "r") as stream:
    try:
       files = (yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
#Fetch file paths
createSchema = files['createTable']['Schema']
createDefinition = files['createTable']['attributeDefinitions']
addData = files['addData']
deleteData = files['deleteData']
getData = files['getItem']
itemsToUpdate = files['updateItem']['itemsToUpdate']
fieldsToUpdate = files['updateItem']['fieldsToUpdate']

def createTable(dynamo,Name):
    try:
        table = dynamo.create_table(
            TableName = Name,
            KeySchema = json.loads(pathlib.Path(createSchema).read_text()),
            AttributeDefinitions = json.loads(pathlib.Path(createDefinition).read_text()),
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
        table.wait_until_exists()
        output = table.item_count
    except botocore.exceptions.ClientError as error:
        output = error

    return output

def addItems(dynamo,name):
    table = dynamo.Table(name)
    items = json.loads(pathlib.Path(addData).read_text())
    result = ""
    for item in items:
        try:
            output = str(table.put_item(
                Item = item
            ))
            #output = str(response['HTTPStatusCode'])
        except botocore.exceptions.ClientError as error:
            output = str(error)
        result+=output
        result+="\n"
    return result

def readTable(dynamo,name):
    table = dynamo.Table(name)
    try:
        items = table.scan()['Items']
    except botocore.exceptions.ClientError as error:
        items = error
    return items
    
def updateData(dynamo,name):
    table = dynamo.Table(name)
    result = ""
    items = json.loads(pathlib.Path(itemsToUpdate).read_text())
    update = json.loads(pathlib.Path(fieldsToUpdate).read_text())
    result = ""
    for i in range(0,len(items)):
        try:
            output = str(table.update_item(
                Key = items[0] |
                update[0]
            ))
        except botocore.exceptions.ClientError as error:
            output = str(error)
        result+=output
        result+="\n"
    return result

def deleteData(dynamo,name):
    table = dynamo.Table(name)
    result = ""
    items = json.loads(pathlib.Path(deleteData).read_text())
    for item in items:
        try:
            output = str(table.delete_item(
                Key = item))
        except botocore.exceptions.ClientError as error:
            output = str(error)
        result+=output
        result+="\n"
    return result


def getItem(dynamo,name):
    table = dynamo.Table(name)
    result = ""
    items = json.loads(pathlib.Path(getData).read_text())
    for item in items:
        try:
            output = str(table.get_item(
                Key = item))
        except botocore.exceptions.ClientError as error:
            output = str(error)
        result+=output
        result+="\n"
    return result





dynamo = boto3.resource('dynamodb')
name = "tests"

#creationStatus = createTable(dynamo,name)
#print(creationStatus)

#insertStatus = addItems(dynamo,name)
#print(insertStatus)

#table = readTable(dynamo,name)
#print(table)

#updateStatus = updateData(dynamo,name)
#print(updateStatus)

#deleteStatus = deleteData(dynamo,name)
#print(deleteData)

get = getItem(dynamo,name)
print(get)