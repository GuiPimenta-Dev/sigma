from infra.services.secrets_manager import SecretsManager
from infra.services.sns import SNS
from infra.services.api_gateway import APIGateway
from infra.services.aws_lambda import AWSLambda
from infra.services.dynamo_db import DynamoDB
from infra.services.layers import Layers


class Services:
    def __init__(self, scope, context) -> None:
        self.api_gateway = APIGateway(scope, context)
        self.sns = SNS(scope, context)
        self.aws_lambda = AWSLambda(scope, context, self.sns.alarms_topic)
        self.layers = Layers(scope)
        self.dynamo_db = DynamoDB(scope, context)
        self.secrets_manager = SecretsManager(scope, context)
