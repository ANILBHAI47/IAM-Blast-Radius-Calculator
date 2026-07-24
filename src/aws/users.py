from .client import get_resources
def get_users():
    return get_resources("iam","list_users","Users")