import boto3
from botocore.exceptions import ClientError
#generic function
def get_relationships(operation,parameter_name,parameter_value,response_key):
    try:
        iam = boto3.client("iam")
        paginator = iam.get_paginator(operation)
        params = {
            parameter_name:parameter_value
        }
        relationships = []
        for page in paginator.paginate(**params):
            relationships.extend(page[response_key])
        
        return relationships
    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        error_message = e.response["Error"]["Message"]
        print(f"error code: {error_code}")
        print(f"error message: {error_message}")
        return [] 
    #wrapper functions 

def get_user_groups(user_name):
    return get_relationships(
        "list_groups_for_user",
        "UserName",
        user_name,
        "Groups"
    )


def get_user_policies(user_name):
    return get_relationships(
        "list_attached_user_policies",
        "UserName",
        user_name,
        "AttachedPolicies"
    )


def get_group_policies(group_name):
    return get_relationships(
        "list_attached_group_policies",
        "GroupName",
        group_name,
        "AttachedPolicies"
    )


def get_role_policies(role_name):
    return get_relationships(
        "list_attached_role_policies",
        "RoleName",
        role_name,
        "AttachedPolicies"
    )
        