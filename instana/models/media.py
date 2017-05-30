from .location import Location
from .user import User


class Media(object):
    """
    Media Model
    """

    class Caption(object):
        """
        Caption Model
        """
        def __init__(self, json: dict={}):
            """
            Initialize Caption Object
            """
            json = json if json else {}
            self._pk = json.get('pk')
            self._text = json.get('text')
            self._type = json.get('type')

    def __init__(self, json: dict):
        """
        Initialize Media Object
        """
        self._taken_at = json.get('taken_at')
        self._pk = json.get('pk')
        self._id = json.get('id')
        self._media_type = json.get('media_type')
        self._code = json.get('code')
        self._location = None
        self._location = Location(json.get('location', {}))
        self._view_count = json.get('view_count')
        self._user = User(json.get('user'))
        self._like_count = json.get('like_count')
        self._has_liked = json.get('has_liked')
        self._comment_count = json.get('comment_count')
        self._caption = self.Caption(json.get('caption', {}))
