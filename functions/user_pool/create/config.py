from infra.services import Services


class CreateConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Create", path="./functions/user_pool", description="Create User Pool Id", directory="create"
        )

        services.api_gateway.create_endpoint("GET", "/user_pool", function, public=True)
