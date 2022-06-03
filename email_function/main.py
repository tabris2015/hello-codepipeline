import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    sns_message = event.get("Sns")
    logger.info(f"EVENT: {sns_message}")
    response = {"result": "OK"}
    return response
