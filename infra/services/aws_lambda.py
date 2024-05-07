from aws_cdk import Duration
from aws_cdk.aws_lambda import Code, Function, Runtime
from lambda_forge import Path, track
from lambda_forge.interfaces import IAWSLambda
from aws_cdk.aws_cloudwatch import Alarm, ComparisonOperator
from aws_cdk.aws_cloudwatch_actions import SnsAction


class AWSLambda(IAWSLambda):
    def __init__(self, scope, context, alarms_topic) -> None:
        self.scope = scope
        self.context = context
        self.alarms_topic = alarms_topic
        self.functions = {}

    @track
    def create_function(
        self,
        name,
        path,
        description,
        directory=None,
        timeout=1,
        layers=[],
        environment={},
    ):

        function = Function(
            scope=self.scope,
            id=name,
            description=description,
            function_name=f"{self.context.stage}-{self.context.name}-{name}",
            runtime=Runtime.PYTHON_3_9,
            handler=Path.handler(directory),
            environment=environment,
            code=Code.from_asset(path=Path.function(path)),
            layers=layers,
            timeout=Duration.minutes(timeout),
        )

        self.functions[name] = function

        alarm = Alarm(
            scope=self.scope,
            id=f"{self.context.stage}-{name}-Alarm",
            metric=function.metric_errors(),
            threshold=1,
            evaluation_periods=1,
            alarm_description="The latest deployment errors > 0",
            alarm_name=f"{self.context.stage}-{name}-Alarm",
            comparison_operator=ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
        )

        alarm.add_alarm_action(SnsAction(topic=self.alarms_topic))
        
        return function
        