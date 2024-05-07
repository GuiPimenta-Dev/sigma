from infra.services import Services

class AlarmConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Alarm",
            path="./functions/alarm",
            description="Send email notifications",
        )
        
        services.sns.create_trigger(services.sns.alarms_topic, function)
