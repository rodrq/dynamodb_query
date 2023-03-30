import boto3
import os
from dotenv import load_dotenv
from settings import *
load_dotenv()



session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name= aws_region #Change in settings.py
)

dynamodb = session.resource('dynamodb')
table = dynamodb.Table(table_name)


query_params = {
    'KeyConditionExpression': '#date = :pk_value',
    'ExpressionAttributeNames': {
        '#date': table_pk 
    }, 
    'ExpressionAttributeValues': {
        ':pk_value': table_value_to_fetch 
    }
}

response = table.query(**query_params)

"""for item in response['Items']:
    print(item)"""

