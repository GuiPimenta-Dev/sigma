from .main import lambda_handler

def test_lambda_handler(table):
    table.put_item(Item={"PK": "1", "SK": "example.com", "weight": 1})
    table.put_item(Item={"PK": "1", "SK": "example1.com", "weight": 2})
    table.put_item(Item={"PK": "2", "SK": "example2.com", "weight": 2})
    table.put_item(Item={"PK": "3", "SK": "example3.com", "weight": 2})

    event = {
        "queryStringParameters": {"pool_id": "1"}
    }
    response = lambda_handler(event, None)
    
    assert response["statusCode"] == 301
    assert response["headers"]["Location"] in ["https://example.com","https://example1.com"]
    
    