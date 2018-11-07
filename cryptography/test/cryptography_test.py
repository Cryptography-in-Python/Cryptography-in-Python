import unittest

from ..DES.cryptography_des import CryptographyDES
from ..RSA.cryptography_rsa import CryptographyRSA

class CryptographyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._DES_instance = CryptographyDES()
        cls._RSA_instance = CryptographyRSA()
        cls._plain_text   = "Nogizaka"


    def testIfDESCanGetPlainTest(self):
        self._DES_instance.set_plain_text(plain_text=self._plain_text)
        plain_txt = self._DES_instance.get_plain_text()

        self.assertEqual(plain_txt, self._plain_text, 
        msg="The plain text in DES instance does not equal to preset plain text")

    def testIfRSAEncipherDecipherIsSymmetric(self):
        self._RSA_instance = CryptographyRSA()
        self._RSA_instance.set_key(key='initial')
        self._RSA_instance.set_plain_text(self._plain_text)
        self._RSA_instance.encrypt()
        self._RSA_instance.decrypt()
        
        def decoder(int_like:int) -> str:
            return bytes([int_like]).decode()

        results = self._RSA_instance.get_plain_text(decode_func=decoder)
        self.assertEqual(
            "".join([mem for mem in results]), 
            self._plain_text,
            msg="RSA cannot decipher its encrypted cipher text"
        )

    @classmethod
    def tearDownClass(cls):
        del cls._DES_instance
        del cls._RSA_instance


if __name__ == "__main__":
    unittest.main()
