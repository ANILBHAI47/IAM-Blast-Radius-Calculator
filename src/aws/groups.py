from .client import get_resources
def get_groups():
    return get_resources("iam","list_groups","Groups")