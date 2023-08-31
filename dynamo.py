import boto3
import json
import pathlib
import botocore


def createTable(dynamo,Name):
    try:
        table = dynamo.create_table(
            TableName = Name,
            KeySchema = json.loads(pathlib.Path("dbScripts/createTable/Schema.json").read_text()),
            AttributeDefinitions = json.loads(pathlib.Path("dbScripts/createTable/AttributeDefinitions.json").read_text()),
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
    items = json.loads(pathlib.Path('dbScripts/addData/items.json').read_text())
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
    restlt = ""
    items = json.loads(pathlib.Path('dbScripts/updateItem/update.json').read_text())
    result = ""
    for item in items:
        try:
            output = str(table.update_item(item))
        except botocore.exceptions.ClientError as error:
            output = str(error)
        result+=output
        result+="\n"
    return result


dynamo = boto3.resource('dynamodb')
name = "test"

creationStatus = createTable(dynamo,name)
print(creationStatus)

#insertStatus = addItems(dynamo,name)
#print(insertStatus)

#table = readTable(dynamo,name)
#print(table)

#updateStatus = updateData(dynamo,name)
#print(updateStatus)