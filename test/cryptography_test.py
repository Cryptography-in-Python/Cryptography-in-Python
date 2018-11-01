import unittest

from ..DES.cryptography_des import CryptographyDES
from ..RSA.cryptography_rsa import CryptographyRSA

class CryptographyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._DES_instance = CryptographyDES()
        cls._plain_text   = "Nogizaka"

    def testIfDESCanGetPlainTest(self):
        self._DES_instance.set_plain_text(plain_text=self._plain_text)
        plain_txt = self._DES_instance.get_plain_text()

        self.assertEqual(plain_txt, self._plain_text, 
        msg="The plain text in DES instance does not equal to preset plain text")

    @classmethod
    def tearDownClass(cls):
        del cls._DES_instance


if __name__ == "__main__":
    unittest.main()
