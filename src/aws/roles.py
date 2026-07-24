from .client import get_resources
def get_roles():
    return get_resources("iam","list_roles","Roles")