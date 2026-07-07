import os
import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = os.environ["TABLE_NAME"]

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

#insert to db
def put_item(item: dict) -> None:
    table.put_item(Item=item)


def query_by_partition_key(partition_key: str) -> list:
    response = table.query(
        KeyConditionExpression=Key("PK").eq(partition_key)
    )
    return response.get("Items", [])