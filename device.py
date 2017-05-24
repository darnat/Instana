import uuid
import hashlib


class Device(object):
    """
    Represent Device like android one
    """

    DEVICE_SETTINTS = {
        'manufacturer': 'Xiaomi',
        'model': 'HM 1SW',
        'android_version': 20,
        'android_release': '4.4.4',
    }

    USER_AGENT = ('Instagram 10.21.0 Android ({android_version}/'
                  '{android_release};'
                  ' 320dpi; 1080x1920; {manufacturer}; {model};'
                  ' armani; qcom; en_US)'.format(**DEVICE_SETTINTS))

    def __init__(self, username):
        self.uuid = str(uuid.uuid4())
        m = hashlib.md5()
        m.update(username.encode('utf-8'))
        self.device_id = self.generate_device_id(m.hexdigest())

    def user_agent(self, appVersion=None):
        """
        return the User Agent of the Device
        """
        return self.USER_AGENT

    def generate_device_id(self, seed):
        """
        Generate a random Device ID
        """
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-{}'.format(m.hexdigest()[:16])
