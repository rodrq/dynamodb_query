import boto3
import os
from settings import *

session = boto3.Session(
    aws_access_key_id= ACCESS_KEY,
    aws_secret_access_key= SECRET_KEY,
    region_name= AWS_REGION
)

dynamodb = session.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)


query_params = {
    'KeyConditionExpression': '#date = :pk_value',
    'ExpressionAttributeNames': {
        '#date': TABLE_PK 
    }, 
    'ExpressionAttributeValues': {
        ':pk_value': VALUE_TO_FETCH
    }
}

response = table.query(**query_params)

"""for item in response['Items']:
    print(item)"""

