class CryptographyVigenere():
	def encrypt(self,input,key):
		ptLen = len(input)
		keyLen = len(key)

		quotient = ptLen // keyLen
		remainder = ptLen % keyLen

		out = ""

		for i in range (0,quotient):
			for j in range (0,keyLen):
				c=int((ord(input[i*keyLen+j])-ord('a')+ord(key[j])-ord('a'))%26+ord('a'))
				out+=chr(c)

		for i in range (0,remainder):
			c=int((ord(input[quotient*keyLen+i])-ord('a')+ord(key[i])-ord('a'))%26+ord('a'))
			out+=chr(c)

		return out

	def decrypt(self,output,key):
		ptLen = len (output) 
		keyLen = len (key)
		
		quotient = ptLen // keyLen
		remainder = ptLen % keyLen

		input = ""
		for i in range (0 , quotient):
			for j in range (0 , keyLen) :
				c = int((ord(output[i*keyLen+j]) - ord('a') - (ord(key[j]) - ord('a')) % 26 + ord('a')))
				input+=chr(c)

		for i in range (0 , remainder) :
			c = int((ord(output[quotient*keyLen + i]) - ord('a') - (ord(key[i]) - ord('a')) % 26 + ord('a')))
			input+=chr(c)  

		return input

if __name__ == "__main__":
	vigenere_instance = CryptographyVigenere()

	plainText = input ("Please input the plainText : ")
	key = input ("Please input the key : ")
	plainTextToCipherText = vigenere_instance.encrypt(plainText , key)
	print(plainTextToCipherText)


	cipherText = input ("Please input the cipherText : ")
	key = input ("Please input the key : ")
	cipherTextToPlainText = vigenere_instance.decrypt(cipherText , key)
	print(cipherTextToPlainText)


	
	
	
