import json
from dataclasses import dataclass
import boto3
import os


@dataclass
class Input:
    email: str


@dataclass
class Output:
    message: str


def lambda_handler(event, context):

    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ.get("ALARMS_TABLE_NAME")
    table = dynamodb.Table(table_name)

    email = event["queryStringParameters"]["email"]

    table.put_item(Item={"PK": email})

    raise Exception("This is a mock error")
