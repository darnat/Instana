import json
import hmac
import hashlib
import urllib

from . import constants


def sign(payload):
    key = constants.PRIVATE_KEY
    json_data = json.dumps(payload)
    signed = hmac.new(key['SIG_KEY'].encode('utf-8'),
                      json_data.encode('utf-8'),
                      hashlib.sha256)
    try:
        parsed_data = urllib.parse.quote(json_data)
    except AttributeError:
        parsed_data = urllib.quote(json_data)
    return {
        'signature': signed.hexdigest(),
        'app_version': key['APP_VERSION'],
        'sig_key_version': key['SIG_VERSION'],
        'payload': parsed_data
    }
