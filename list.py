import json
import datetime
import boto3

table = boto3.resource('dynamodb').Table('bolt-pass-resources')

def handler(event, context):
    print('Event: ' + json.dumps(event))
    response = table.get_item(Key={ 'id': 'id-1' })
    print('DynamoDB Response: ' + json.dumps(response))

    data = {
        'output': 'Hello World List',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
