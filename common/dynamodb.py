import boto3
import os

TABLE_NAME = os.environ.get("TABLE_NAME")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def put_item(item):
    table.put_item(Item=item)


def query_items(pk):
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key("PK").eq(pk)
    )
    return response.get("Items", [])