from .device import Device
from .request import Request
from .models.media import Media
from .collections.medias import Medias
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
        print(res.text)
        medias = Medias([Media(media) for media in res.json().get(('ranked'
                                                                   '_items'))])
        medias._next_max_id = res.json().get('next_max_id')
        return medias

    def get_location_feed(self, location_id: int):
        """
        Get Location Feed
        """
        res = Request(self._session)\
            .set_resource('locationFeed',
                          {'id': location_id,
                           'maxID': '',
                           'rankToken': self._session.get_rank_token()})\
            .set_method('GET')\
            .set_device(self._device)\
            .send()
        medias = Medias([Media(media) for media in res.json().get(('ranked'
                                                                   '_items'))])
        medias._next_max_id = res.json().get('next_max_id')
        return medias
