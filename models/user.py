

class User(object):
    """
    User Model
    """
    def __init__(self, json: dict):
        self._pk = json.get('pk')
        self._username = json.get('username')
        self._full_name = json.get('full_name')
        self._is_private = json.get('is_private')
        self._profile_pic_url = json.get('profile_pic_url')
        self._profile_pic_id = json.get('profile_pic_id')
        self._is_verified = json.get('is_verified')
        self._has_anonymous_profile_picture = json.get(('has_anonymous'
                                                        '_profile_picture'))
        self._allow_contacts_sync = json.get('allow_contacts_sync')
        self._fbuid = json.get('fbuid')

    def get_id(self):
        return self._pk
