
class CryptographyVigenere(object):

	def __init__(self):
		self._start_from = 32
		self._end_to     = 127

	def get_cipher_alpha(self, plain_letter:int, key_letter:int) -> int:
		offset = key_letter - self._start_from
		row    = list(range(self._start_from + offset, self._end_to)) +\
		list(range(self._start_from, self._start_from + offset))

		return row[plain_letter - self._start_from]

	def get_plain_alpha(self, cipher_letter:int, key_letter:int) -> int:
		offset = key_letter - self._start_from
		row    = list(range(self._start_from + offset, self._end_to)) +\
		list(range(self._start_from, self._start_from + offset))

		return row.index(cipher_letter) + self._start_from

	@staticmethod
	def pad_key(key:str, length:int) -> str:
		while len(key) < length:
			key += key
		return key[:length]
	
	def encrypt(self, plain_text:str, key:str) -> str:
		result = []
		key = CryptographyVigenere.pad_key(key, len(plain_text))

		for plain, k in zip(plain_text, key):
			result.append(chr(self.get_cipher_alpha(ord(plain), ord(k))))
		return "".join(result)

	def decrypt(self, cipher_text:str, key:str) -> str:
		result = []
		key = CryptographyVigenere.pad_key(key, len(cipher_text))

		for cipher, k in zip(cipher_text, key):
			result.append(chr(self.get_plain_alpha(ord(cipher), ord(k))))
		return "".join(result)


if __name__ == "__main__":
	vigenere_instance = CryptographyVigenere()
	cipher = vigenere_instance.encrypt("Hello World! From Jerome???", "blaha")
	plain  = vigenere_instance.decrypt(cipher, "blaha")
	print("cipher is", cipher)
	print("plain is", plain)


	
	
	
