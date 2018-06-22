from unittest import TestCase

from iw_utils.utils import Util


class UtilsTest(TestCase):
    def test_encrypted_string(self):
        plaint_text = 'test'
        encrypted_string = Util.encrypt3DESData('testkey',plaint_text)
        print(encrypted_string)
        self.assertNotEqual(plaint_text, encrypted_string)

    def test_decrypted_string(self):
        encrypted_text = 'cinQDDzrFSk='
        decrypted_text = Util.decrypt3DESData('testkey',encrypted_text)
        self.assertNotEqual(decrypted_text, encrypted_text)

    def test_generate_token_is_not_none(self):
        token = Util.generate_token()
        self.assertIsNotNone(token)

    def test_generate_token_is_unique(self):
        token = Util.generate_token()
        token2 = Util.generate_token()
        self.assertNotEqual(token, token2)

    def test_generate_token_is_not_none(self):
        token = Util.generate_random_base32()
        self.assertIsNotNone(token)

    def test_generate_token_is_unique(self):
        token = Util.generate_random_base32()
        token2 = Util.generate_random_base32()
        self.assertNotEqual(token, token2)
