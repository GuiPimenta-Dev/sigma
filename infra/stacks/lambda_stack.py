from functions.alarm.config import AlarmConfig
from aws_cdk import Stack
from constructs import Construct
from lambda_forge import release

from docs.config import DocsConfig
from functions.redirect.config import RedirectConfig
from functions.pool.create.config import CreateConfig
from functions.pool.list.config import ListConfig
from infra.services import Services


@release
class LambdaStack(Stack):
    def __init__(self, scope: Construct, context, **kwargs) -> None:

        super().__init__(scope, f"{context.stage}-{context.name}-Lambda-Stack", **kwargs)

        self.services = Services(self, context)

        # Docs
        DocsConfig(self.services)

        # Redirect
        RedirectConfig(self.services)

        # UserPool
        ListConfig(self.services)
        CreateConfig(self.services)

        # Alarm
        AlarmConfig(self.services)
