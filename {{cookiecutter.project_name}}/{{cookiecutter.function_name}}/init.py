import json
import os
import boto3
from aws_lambda_powertools import Logger

logger = Logger()

def lambda_handlr(event, context):
    try:
        # Enter your code 
        logger.info("This is a test")
    except Exception as error:
        logger.exception(f"EXCEPTION : {error}")
        raise
    else:
        return {
            "status_code" : 200,
            "body" : json.dumps({
                "message" : "HelloWorld"
            })
        }
