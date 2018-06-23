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
    def encrypt3DESData(key: str, plain_text: str) -> str:
        """Provides encryption for plaintext content required in request data.

        :param key:
            - String encryption key
        :param plain_text:
            - String to be encrypted

        :return str: encrypted text

        """

        data = plain_text

        encoded_key = key.encode("ascii")
        m = hashlib.md5()
        m.update(encoded_key)
        hex_key = m.digest()
        k = triple_des(hex_key, ECB, padmode=PAD_PKCS5)
        d = base64.b64encode(k.encrypt(data))
        return d.decode("ascii")


    

    @staticmethod
    def decrypt3DESData(key, ciphertext):
        """Provides decryption for encrypted content returned from flutterwave service.

        :param key:
            - decryption key

        :param ciphertext:
            - encrypted string

        :return str:
            Decrypted string

        """
        encoded_key = key.encode("ascii")
        m = hashlib.md5()
        m.update(encoded_key)
        hex_key = m.digest()
        k = triple_des(hex_key, ECB, padmode=PAD_PKCS5)

        d = k.decrypt(base64.b64decode(ciphertext))

        return d.decode("ascii")




    @staticmethod
    def generate_token():
        """Generate token

        :return str: uuid as string
        """
        return uuid.uuid4().hex



    @staticmethod
    def generate_random_base32():
        """
        Generate a random base32 string

        :return str: random base32 string
        """
        return pyotp.random_base32()




    @staticmethod
    def generate_totp(seed, otp_interval=300):
        """
        Generate a time based OTP
        :param seed:
            - previously generated base32 string
        :param optional otp_interval:
            - TOTP validity timeout

        :return str: TOTP as string
        """
        return pyotp.TOTP(seed, interval=otp_interval).now()



    @staticmethod
    def verify_totp(seed, otp, interval=300):
        """
        Verify previously generated time based OTP

        :param seed:
            - previously generated base32 string
        :param otp:
            - OTP value to verify
        :param optional interval:
            - validity period used to generate token

        :return Boolean:
        """
        return pyotp.TOTP(seed, interval=interval).verify(otp)
