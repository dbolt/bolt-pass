import json
import datetime
import boto3
from boto3.dynamodb.conditions import Key

QUERY_STRING_PARAMS_KEY = 'queryStringParameters'
ROOT_KEY = 'root'
RESOURCES_TABLE = 'bolt-pass-resources-1'

table = boto3.resource('dynamodb').Table(RESOURCES_TABLE)

def handler(event, context):
    print('Event: ' + json.dumps(event))

    prefix = get_root(event)
    if root is None:
        response = table.scan()
    else:
        response = table.query(
            KeyConditionExpression=Key(ROOT_KEY).eq(root)
        )

    print('DynamoDB Response: ' + json.dumps(response))

    data = {
        'output': 'Hello World List',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'response': response
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

def get_root(event): 
    params = event.get(QUERY_STRING_PARAMS_KEY, {})
    if params is None:
        params = {}
    return params.get(PREFIX_KEY, '')
