import boto3
from botocore.exceptions import ClientError


def parse_policy(policy):
    """
    Downloads a policy document and returns all allowed actions.
    """

    try:
        # Extract required information
        arn = policy["Arn"]
        version = policy["DefaultVersionId"]

        # Create IAM client
        iam = boto3.client("iam")

        # Fetch policy document
        response = iam.get_policy_version(
            PolicyArn=arn,
            VersionId=version
        )

        # Extract document
        document = response["PolicyVersion"]["Document"]

        # Get all statements
        statements = document["Statement"]

        # If only one statement exists, AWS may return a dictionary
        if isinstance(statements, dict):
            statements = [statements]

        permissions = []

        # Extract allowed actions
        for statement in statements:

            if statement.get("Effect") != "Allow":
                continue

            actions = statement.get("Action", [])

            if isinstance(actions, str):
                actions = [actions]

            permissions.extend(actions)

        return permissions

    except ClientError as e:
        print(f"Error Code: {e.response['Error']['Code']}")
        print(f"Reason: {e.response['Error']['Message']}")
        return []