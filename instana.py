from .device import Device
from .request import Request
from .models.media import Media
from . import session as Session


class Instana(object):
    """
    Main API class
    """
    def __init__(self):
        """
        Initialize params
        """
        self._session = None
        self._device = None

    def login(self, username: str, password: str):
        """
        Login a user with credentials
        """
        self._device = Device(username)
        self._session = Session.create(self._device, username, password)

    def get_tag_feed(self, tag: str):
        """
        Get Tag Feed
        """
        res = Request(self._session)\
            .set_resource('tagFeed',
                          {'tag': tag,
                           'maxID': '',
                           'rankToken': self._session.get_rank_token()})\
            .set_method('GET')\
            .set_device(self._device)\
            .send()
        medias = [Media(media) for media in res.json().get('ranked_items')]
        return medias
