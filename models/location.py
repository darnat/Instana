

class Location(object):
    """
    Location object
    """
    def __init__(self, json: dict):
        self._pk = json.get('pk')
        self._name = json.get('name')
        self._address = json.get('address')
        self._city = json.get('city')
        self._short_name = json.get('short_name')
        self._lng = json.get('lng')
        self._lat = json.get('lat')
