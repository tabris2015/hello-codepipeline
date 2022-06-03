import os
import boto3

sns_client = boto3.client("sns")
sns_topic_arn = os.environ.get("SNS_TOPIC_ARN")


def get_sns_client():
    yield sns_client
