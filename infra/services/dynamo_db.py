from aws_cdk import aws_dynamodb as dynamo_db
from aws_cdk import aws_iam as iam


class DynamoDB:
    def __init__(self, scope, context) -> None:

        self.pool_table = dynamo_db.Table.from_table_arn(
            scope,
            "PoolTable",
            "arn:aws:dynamodb:us-east-2:211125768252:table/Redirect"
        )
        

    @staticmethod
    def add_query_permission(table, function):
        function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Query"],
                resources=[f"{table.table_arn}/index/*"],
            )
        )
