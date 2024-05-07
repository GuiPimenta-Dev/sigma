import os

import boto3
import moto
import pytest

@pytest.fixture
def env():
    os.environ["POOL_TABLE_NAME"] = "MOCK"


@pytest.fixture
def table(env):
    with moto.mock_dynamodb():
        db = boto3.client("dynamodb")
        db.create_table(
            TableName="MOCK",
            KeySchema=[
                {"AttributeName": "PK", "KeyType": "HASH"},
                {"AttributeName": "SK", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )

        table = boto3.resource("dynamodb").Table("MOCK")
        yield table