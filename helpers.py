import uuid


def generate_UUID():
    """
    Generate a UUID and return it
    """
    return str(uuid.uuid4())


def generate_rank_token(id: int):
    """
    Generate a rank token and return it
    """
    return str(id) + '_' + generate_UUID()
