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
dynamo = boto3.resource('dynamodb', region_name ="ap-southeast-1")

def createTable(name):
    try:
        table = dynamo.create_table(
            Tablename = name,
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

def addData(name):
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

def readTable(name):
    table = dynamo.Table(name)
    try:
        items = table.scan()['Items']
    except botocore.exceptions.ClientError as error:
        items = error
    return items
    
def updateItems(name):
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

def deleteData(name):
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


def getItem(name):
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






name = "tests"

#creationStatus = createTable(name)
#print(creationStatus)

#insertStatus = addItems(name)
#print(insertStatus)

#table = readTable(name)
#print(table)

#updateStatus = updateData(name)
#print(updateStatus)

#deleteStatus = deleteData(name)
#print(deleteData)

get = getItem(name)
print(get)