PLAIN_TEXT_FILE = './plain_text.txt'
CIPHER_TEXT_FILE = './cipher_text.txt'
KEY = 3

def read_file(path):
	content = []
	with open(path, 'r') as f:
		for line in f:
			content.append(line)
	return content

def write_to_file(path, message):
	with open(path, 'w') as f:
		for line in message:
			f.write(line)

def encrypt(plain_text):
	encrypted = []
	for line in plain_text:
		this_line = ''
		for char in line:
			if not char==' ':
				this_character = chr(ord(char)+KEY)
			else:
				this_character = ' '
			this_line += this_character
		encrypted.append(this_line)
	return encrypted

def decrypt(cipher_text):
	plain_text = []
	for line in cipher_text:
		this_line = ''
		for char in line:
			if not char==' ':
				this_character = chr(ord(char)-KEY)
			else:
				this_character = ' '
			this_line += this_character
		plain_text.append(this_line)
	return plain_text

def encryption():
	plain_text = read_file(PLAIN_TEXT_FILE)
	encrypted_version = encrypt(plain_text)
	write_to_file(CIPHER_TEXT_FILE, encrypted_version)
	print(encrypted_version)

def decryption():
	cipher_text = read_file(CIPHER_TEXT_FILE)
	plain_text = decrypt(cipher_text)
	print(plain_text)

def main():
	print('Encrypting...')
	encryption()
	print('Dencrypting...')
	decryption()
	

if __name__ == '__main__':
	main()