import os
import boto3

stage = os.environ.get("STAGE", "local")
ssm = boto3.client("ssm")

table_name = (
    ssm.get_parameter(Name=f"table-name-{stage}")["Parameter"]["Value"]
    if stage != "local"
    else "users-local"
)
print(f"Table Name: {table_name}")

dynamodb = boto3.resource(
    "dynamodb", endpoint_url="http://localhost:8000" if stage == "local" else None
)
table = dynamodb.Table(table_name)
