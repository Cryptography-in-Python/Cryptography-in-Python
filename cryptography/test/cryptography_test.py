import unittest

from ..DES.cryptography_des import CryptographyDES
from ..RSA.cryptography_rsa import CryptographyRSA

class CryptographyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._DES_instance = CryptographyDES()
        cls._RSA_instance = CryptographyRSA()
        cls._plain_text   = "Nogizaka"

        cls._cipher_text_RSA  = None


    def testIfDESCanGetPlainTest(self):
        self._DES_instance.set_plain_text(plain_text=self._plain_text)
        plain_txt = self._DES_instance.get_plain_text()

        self.assertEqual(plain_txt, self._plain_text, 
        msg="The plain text in DES instance does not equal to preset plain text")

    def testIfRSAEncipherDecipherIsSymmetric(self):
        # =========== Key Generation & Encryption ====================
        self._RSA_instance.set_key(key='initial')
        self._RSA_instance.set_plain_text(self._plain_text)
        self._RSA_instance.encrypt()
        self._cipher_text_RSA = self._RSA_instance.get_cipher_text_as_bytes()

        # ============ Decryption ============
        self._RSA_instance.set_cipher_text(self._cipher_text_RSA)
        self._RSA_instance.decrypt()
        result = self._RSA_instance.get_plain_text_as_string()
        self.assertEqual(
            result, 
            self._plain_text,
            msg="RSA cannot decipher its encrypted cipher text"
        )

    @classmethod
    def tearDownClass(cls):
        del cls._DES_instance
        del cls._RSA_instance


if __name__ == "__main__":
    unittest.main()
