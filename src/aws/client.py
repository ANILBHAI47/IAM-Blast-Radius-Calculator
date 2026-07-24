import boto3
from botocore.exceptions import ClientError

def get_resources(service_name, operation, response_key):
    try:
        service = boto3.client(service_name)

        all_resources = []

        paginator = service.get_paginator(operation)

        for page in paginator.paginate():
            all_resources.extend(page[response_key])

        return all_resources

    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        error_message = e.response["Error"]["Message"]

        print(f"Error Code: {error_code}")
        print(f"Reason: {error_message}")

        return []