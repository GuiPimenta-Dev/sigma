from aws_cdk.aws_sns import Topic
from aws_cdk import aws_lambda_event_sources


class SNS:
    def __init__(self, scope, context) -> None:
        self.context = context

        self.alarms_topic = Topic.from_topic_arn(
            scope,
            id="AlarmsTopic",
            topic_arn="arn:aws:sns:us-east-2:211125768252:Alarms",
        )

    def create_trigger(self, topic, function, stages=None):
        if stages and self.context.stage not in stages:
            return

        sns_subscription = aws_lambda_event_sources.SnsEventSource(topic)
        function.add_event_source(sns_subscription)
