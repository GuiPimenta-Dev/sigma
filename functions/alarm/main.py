import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3
import sm_utils


def lambda_handler(event, context):

    # Fetch the SMTP details from the environment variables
    SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = os.environ.get("SMTP_PORT", "465")

    # Get the secret name from env variable
    SECRET_NAME = os.environ.get("SECRET_NAME", "mailer")

    # Get the secret from sm_utils layer
    secret = sm_utils.get_secret(SECRET_NAME)

    SMTP_USER = secret["email"]
    SMTP_PASS = secret["password"]

    # Create the multipart email
    msg = MIMEMultipart()
    sender_name = "Sigma"

    # Set the 'From' field, including both the name and the email:
    msg["From"] = f"{sender_name} <{SMTP_USER}>"
    msg["Subject"] = "Alarm Notification"

    # Join the current directory with the filename to get the full path of the HTML file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_directory, "template.html")

    # Read the HTML content
    function_name = json.loads(event["Records"][0]["Sns"]["Message"])["Trigger"]["Dimensions"][0]["value"]
    html = open(html_path).read().replace("{{ lambdaFunction }}", function_name)
    msg.attach(MIMEText(html, "html"))

    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ.get("ALARMS_TABLE_NAME", "ALARMS")
    table = dynamodb.Table(table_name)

    receivers = table.scan()["Items"]

    for receiver in receivers:
        msg["To"] = receiver["PK"]

        # Send the email via Gmail's SMTP server, or use another server if not using Gmail
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, receiver["PK"], msg.as_string())
