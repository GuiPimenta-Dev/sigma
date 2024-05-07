from infra.services import Services


class ListConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="List", path="./functions/pool", description="List User Pool", directory="list"
        )

        services.api_gateway.create_endpoint("GET", "/pool", function, public=True)
