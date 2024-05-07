import os
import random
from dataclasses import dataclass

import boto3


@dataclass
class Path:
    pool_id: str


@dataclass
class Input:
    pass


@dataclass
class Output:
    message: str


def lambda_handler(event, context):
    # Retrieving the DynamoDB table name from environment variable
    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ.get("POOL_TABLE_NAME")
    table = dynamodb.Table(table_name)

    pool_id = event["pathParameters"]["pool_id"]

    # Retrieving the pool from DynamoDB
    response = table.query(KeyConditionExpression="PK = :pk", ExpressionAttributeValues={":pk": pool_id})
    pool = response["Items"]

    # Extracting domains and weights from the pool
    domains = [item["SK"] for item in pool]
    weights = [int(item["weight"]) for item in pool]

    # Choosing a domain based on the weights
    selected_domain = random.choices(domains, weights=weights, k=1)[0]

    # Redirecting to the selected domain
    redirect_url = f"https://{selected_domain}"

    return {"statusCode": 301, "headers": {"Location": redirect_url}}
