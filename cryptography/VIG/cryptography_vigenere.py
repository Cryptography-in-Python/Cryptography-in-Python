class CryptographyVigenere():
	def encrypt(self, input, key):
		ptLen = len(input)
		keyLen = len(key)

		quotient = ptLen // keyLen
		remainder = ptLen % keyLen

		out = ""

		for i in range(0, quotient):
			for j in range(0, keyLen):
				c = (ord(input[i*keyLen+j]) + ord(key[j])) % 126
				out += chr(c)

		for i in range(0, remainder):
			c = (ord(input[quotient*keyLen+i])+ord(key[i])) % 126
			out += chr(c)

		return out

	def decrypt(self, output, key):
		ptLen=len(output)
		keyLen=len(key)

		quotient=ptLen // keyLen
		remainder=ptLen % keyLen

		input=""
		for i in range(0, quotient):
			for j in range(0, keyLen):
				c=ord(output[i*keyLen+j]) - ord(key[j])
				if c < 0:
					c += 126
				input += chr(c)

		for i in range(0, remainder):
			c=ord(output[quotient*keyLen + i]) - ord(key[i])
			if c < 0:
				c += 126
			input += chr(c)

		return input

if __name__ == "__main__":
	vigenere_instance=CryptographyVigenere()

	plainText=input("Please input the plainText : ")
	key=input("Please input the key : ")
	plainTextToCipherText=vigenere_instance.encrypt(plainText, key)
	print(plainTextToCipherText)


	# cipherText = input ("Please input the cipherText : ")
	# key = input ("Please input the key : ")
	cipherTextToPlainText=vigenere_instance.decrypt(plainTextToCipherText, key)
	print(cipherTextToPlainText)
