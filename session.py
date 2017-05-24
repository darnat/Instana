import uuid

from .request import Request
from .device import Device


class Session(object):
    """
    Initialize the Session constructor
    """

    def __init__(self, device: Device):
        self._device = device

    def get_device(self):
        return self._device

    def CSRF_token(self):
        return 'missing'

    @staticmethod
    def login(session, username: str, password: str):
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
        print(response.text)
        return session


def create(device: Device, username: str, password: str):
    session = Session(device)
    return Session.login(session, username, password)
