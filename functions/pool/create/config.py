from infra.services import Services


class CreateConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Create",
            path="./functions/pool",
            description="Create User Pool Id",
            directory="create",
            environment={
                "POOL_TABLE_NAME": services.dynamo_db.pool_table.table_name,
            },
        )

        services.api_gateway.create_endpoint("POST", "/pool", function, public=True)

        services.dynamo_db.pool_table.grant_write_data(function)
