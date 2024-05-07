import json
from .main import lambda_handler


def test_lambda_handler(table):
    table.put_item(Item={"PK": "pool_id", "SK": "example.com", "weight": "1"})
    table.put_item(Item={"PK": "pool_id", "SK": "example1.com", "weight": "2"})
    table.put_item(Item={"PK": "pool_id_2", "SK": "example2.com", "weight": "3"})
    table.put_item(Item={"PK": "pool_id_3", "SK": "example3.com", "weight": "4"})

    response = lambda_handler(None, None)

    assert json.loads(response["body"]) == [
        {"PK": "pool_id", "SK": "example.com", "weight": "1"},
        {"PK": "pool_id", "SK": "example1.com", "weight": "2"},
        {"PK": "pool_id_2", "SK": "example2.com", "weight": "3"},
        {"PK": "pool_id_3", "SK": "example3.com", "weight": "4"},
    ]
