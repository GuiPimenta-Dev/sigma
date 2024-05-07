from infra.services import Services


class AlarmConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Alarm",
            path="./functions/alarm",
            description="Send email notifications",
            layers=[services.layers.sm_utils_layer],
            environment={
                "SMTP_HOST": "smtp.gmail.com",
                "SMTP_PORT": "465",
                "SECRET_NAME": services.secrets_manager.gmail_secret.secret_name,
                "ALARMS_TABLE_NAME": services.dynamo_db.alarms_table.table_name,
            },
        )

        services.sns.create_trigger(services.sns.alarms_topic, function)

        services.secrets_manager.gmail_secret.grant_read(function)

        services.dynamo_db.alarms_table.grant_read_data(function)
