from infra.services import Services


class RedirectConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Redirect",
            path="./functions/redirect",
            description="A function to redirect based on user pool id",
        )

        services.api_gateway.create_endpoint("POST", "/redirect/{pool_id}", function, public=True)
        
        services.dynamo_db.add_query_permission(services.dynamo_db.pool_table, function)
