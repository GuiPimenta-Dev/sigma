import json
import os
from dataclasses import dataclass

import boto3


@dataclass
class Input:
    pass


@dataclass
class Output:
    message: str


def lambda_handler(event, context):

    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ.get("POOL_TABLE_NAME")
    table = dynamodb.Table(table_name)

    pools = table.scan()["Items"]

    return {"statusCode": 200, "body": json.dumps(pools)}
