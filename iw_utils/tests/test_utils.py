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
