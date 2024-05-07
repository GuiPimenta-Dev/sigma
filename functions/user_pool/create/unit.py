import json

from .main import lambda_handler


def test_lambda_handler(table):

    event = {
        "body": json.dumps(
            {
                "pool": [
                    {"domain": "example.com", "weight": "1"},
                    {"domain": "example1.com", "weight": "2"},
                    {"domain": "example2.com", "weight": "3"},
                    {"domain": "example3.com", "weight": "4"},
                ]
            }
        )
    }

    response = lambda_handler(event, None)
    pool_id = json.loads(response["body"])["pool_id"]

    pool = table.query(KeyConditionExpression="PK = :pk", ExpressionAttributeValues={":pk": pool_id})["Items"]
    assert pool == [
        {"PK": pool_id, "SK": "example.com", "weight": "1"},
        {"PK": pool_id, "SK": "example1.com", "weight": "2"},
        {"PK": pool_id, "SK": "example2.com", "weight": "3"},
        {"PK": pool_id, "SK": "example3.com", "weight": "4"},
    ]
