import requests
import uuid
import time

from . import constants
from . import routes
from . import helpers
from .signature import sign
from .device import Device


class Request(object):
    default_headers = {
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3QI=',
        'Accept-Language': 'en-US',
        'Host': constants.HOSTNAME,
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Connection': 'Close',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    def __init__(self, session=None):
        """
        Constructor of the request
        """
        self._url = None
        self._signed_data = False
        self._device = None
        self._request = {}
        self._request['method'] = 'GET'
        self._request['data'] = {}
        self._request['cookies'] = {}
        self._request['headers'] = {}
        self._request['headers'].update(self.default_headers)
        self.set_session(session)

    def set_method(self, method: str):
        """
        Change Request Method
        """
        self._request['method'] = method
        return self

    def set_session(self, session):
        """
        Set Session
        """
        self._session = session
        self.set_CSRF_token(session.CSRF_token())
        self.set_session_id(session.get_session_id())
        return self

    def set_session_id(self, session_id: str):
        """
        Set session id
        """
        self.set_cookie({'sessionid': session_id})
        return self

    def set_CSRF_token(self, token: str):
        """
        Set CSRFToken
        """
        self.set_data({'_csrftoken': token})
        self.set_cookie({'csrftoken': token})
        return self

    def set_resource(self, resource: str, data={}):
        """
        Change Resource
        """
        self.set_URL(routes.get_URL(resource, data))
        return self

    def set_URL(self, url: str):
        """
        Set url
        """
        self._url = url
        return self

    def set_device(self, device: Device):
        """
        Set device
        """
        self._device = device
        self.set_headers({'User-Agent': device.user_agent()})
        self.set_data({'device_id': device.device_id})
        return self

    def set_headers(self, headers: dict, override: bool=False):
        """
        Set headers
        """
        if override:
            self._request['headers'] = headers
        else:
            self._request['headers'].update(headers)
        return self

    def set_data(self, data: dict={}, override: bool = False):
        """
        Set Data
        """
        if override:
            self._request['data'] = data
        else:
            self._request['data'].update(data)
        return self

    def set_cookie(self, cookie: dict={}, override: bool = False):
        """
        Set Cookie
        """
        if override:
            self._request['cookies'] = cookie
        else:
            self._request['cookies'].update(cookie)
        return self

    def sign_payload(self):
        """
        Set Boolean Sign Payload to true
        """
        self._signed_data = True
        return self

    def generate_UUID(self):
        """
        Generate a UUID for the request
        """
        self.set_data({'_uuid': helpers.generate_UUID()})
        return self

    def sign_data(self):
        """
        Sign the Payload
        """
        data = sign(self._request['data'])
        self.set_headers({
            'User-Agent': self._device.user_agent(data['app_version'])
        })
        return ('ig_sig_key_version={sig_key_version}&'
                'signed_body={signature}.{payload}'.format(**data))

    def prepare_data(self):
        """
        Prepare Data for the request
        """
        if self._signed_data:
            self._request['data'] = self.sign_data()

    def send(self):
        """
        Send the request
        """
        self.prepare_data()
        s = requests.session()
        s.headers.update(self._request['headers'])
        if self._request['method'] == 'POST':
            return s.post(self._url, data=self._request['data'],
                          cookies=self._request['cookies'])
        elif self._request['method'] == 'GET':
            return s.get(self._url, cookies=self._request['cookies'])
