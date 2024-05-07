from infra.services import Services


class ListConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="List", path="./functions/user_pool", description="List User Pool", directory="list"
        )

        services.api_gateway.create_endpoint("GET", "/user_pool", function, public=True)
