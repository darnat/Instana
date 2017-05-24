from . import constants


def get_URL(key: str, data={}) -> str:
    return constants.API_ENDPOINT + constants.ROUTES[key].format(**data)
