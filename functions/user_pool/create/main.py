import json
from dataclasses import dataclass
from typing import List
import uuid
import os
import boto3

@dataclass
class Pool:
    domain: str
    weight: int

@dataclass
class Input:
    pool: List[Pool]

@dataclass
class Output:
    pool_id: str


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('POOL_TABLE_NAME')
    table = dynamodb.Table(table_name)

    pool = json.loads(event["body"])["pool"]
    
    pool_id = str(uuid.uuid4())
    
    for item in pool:
        table.put_item(Item={"PK": pool_id, "SK": item["domain"], "weight": item["weight"]})
        
    return {
        "statusCode": 200,
        "body": json.dumps({"pool_id": pool_id})
    }
