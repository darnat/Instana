import uuid
import json

from . import helpers
from .request import Request
from .device import Device
from .exceptions import *
from .models.user import User


class Session(object):
    """
    Initialize the Session constructor
    """

    def __init__(self, device: Device):
        """
        Initialize the Session object
        """
        self._device = device
        self._csrf = None
        self._session_id = None
        self._user = None
        self._rank_token = None

    def get_device(self):
        """
        Return the current associated Device
        """
        return self._device

    def CSRF_token(self):
        """
        Get the csrf Token
        """
        return self._csrf if self._csrf is not None else 'missing'

    def get_session_id(self):
        """
        Get the session id
        """
        return self._session_id

    def get_user(self):
        """
        Return the owner Session User
        """
        return self._user

    def get_rank_token(self):
        """
        Return the rank token of the user
        """
        return self._rank_token

    def set_csrf(self, token: str=None):
        """
        Set the CSRF Token
        """
        self._csrf = token

    def set_session_id(self, session_id: str=None):
        """
        Set the CSRF Token
        """
        self._session_id = session_id

    def set_user(self, user: User=None):
        """
        Set the User
        """
        self._rank_token = helpers.generate_rank_token(user.get_id())
        self._user = user

    @staticmethod
    def login(session, username: str, password: str):
        """
        Static Method provide a way to log in a user with credentials
        """
        data = {
            'username': username,
            'device_id': session.get_device().device_id,
            'password': password,
            'login_attempt_count': '0'
        }
        request = Request(session)\
            .set_resource('login')\
            .set_method('POST')\
            .set_device(session.get_device())\
            .generate_UUID()\
            .set_data(data)\
            .sign_payload()
        response = request.send()
        if response.status_code == 200:
            session.set_session_id(response.cookies['sessionid'])
            session.set_csrf(response.cookies['csrftoken'])
            session.set_user(User(response.json()['logged_in_user']))
            return session
        else:
            try:
                data_response = response.json()
            except Exception as e:
                raise LoginFailed('test')
            if 'invalid_credentials' in data_response:
                if data_response['error_type'] == 'invalid_user':
                    raise InvalidUser()
                elif data_response['error_type'] == 'bad_password':
                    raise InvalidPassword()
                else:
                    raise InvalidCredentials(data_response['error_type'])
            raise LoginFailed()


def create(device: Device, username: str, password: str):
    """
    Method that create a session and log the user
    """
    session = Session(device)
    return Session.login(session, username, password)
