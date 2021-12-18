import secrets
import hmac
import hashlib

class RoundSession(object):

    def __init__(self, message):
        self.message = message
        key = secrets.token_bytes(32)
        self.key = key.hex()
        self.hmac = hmac.new(key, message.encode('utf-8'), hashlib.sha3_256).hexdigest()
        pass

    
