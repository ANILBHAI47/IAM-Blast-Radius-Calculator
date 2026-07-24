import boto3

def get_policies():
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_policies")

    policies = []

    for page in paginator.paginate(Scope="Local"):
        policies.extend(page["Policies"])

    return policies