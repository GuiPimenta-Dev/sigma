from infra.services import Services

class ErrorConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Error",
            path="./functions/error",
            description="A mock of an error",
            environment={
                "ALARMS_TABLE_NAME": services.dynamo_db.alarms_table.table_name,
            },
        )

        services.api_gateway.create_endpoint("GET", "/error", function, public=True)
        
        services.dynamo_db.alarms_table.grant_write_data(function)

            