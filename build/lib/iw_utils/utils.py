import base64
import hashlib
import pyotp
import uuid
from pyDes import triple_des, PAD_PKCS5, ECB


class Util(object):
    @staticmethod
    def enum(**named_values):
        return type('Enum', (), named_values)

    @staticmethod
    def encrypt3DESData(key, plainText):
        """Provides encryption for plaintext content required in request data."""

        data = plainText

        encoded_key = key.encode("ascii")
        m = hashlib.md5()
        m.update(encoded_key)
        hex_key = m.digest()
        k = triple_des(hex_key, ECB,padmode=PAD_PKCS5)
        d = base64.b64encode(k.encrypt(data))
        return d.decode("ascii")

    @staticmethod
    def decrypt3DESData(key, ciphertext):
        """Provides decryption for encrypted content returned from flutterwave service"""
        encoded_key = key.encode("ascii")
        m = hashlib.md5()
        m.update(encoded_key)
        hex_key = m.digest()
        k = triple_des(hex_key, ECB,padmode=PAD_PKCS5)

        d = k.decrypt(base64.b64decode(ciphertext))

        return d.decode("ascii")

    @staticmethod
    def generate_token():
        return uuid.uuid4().hex


    @staticmethod
    def generate_random_base32():
        return pyotp.random_base32()
