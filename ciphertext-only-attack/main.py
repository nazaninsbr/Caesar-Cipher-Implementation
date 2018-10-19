from textblob import TextBlob

CIPHER_TEXT_FILE = './cipher_text.txt'

def read_file(path):
	content = []
	with open(path, 'r') as f:
		for line in f:
			content.append(line)
	return content

def decrypt(cipher_text, key):
	plain_text = []
	for line in cipher_text:
		this_line = ''
		for char in line:
			if not char==' ':
				this_character = chr(ord(char)-key)
			else:
				this_character = ' '
			this_line += this_character
		plain_text.append(this_line)
	return plain_text

def can_we_detect_language(plain_text):
	print(plain_text[0])
	b = TextBlob(plain_text[0])
	lang = b.detect_language()
	if lang=='en':
		return True
	return False

def findPossiblePlainTexts(cipher_text):
	for k in range(0, 26):
		plain_text = decrypt(cipher_text, k)
		if can_we_detect_language(plain_text):
			print('K = {}, Plain Text = {} '.format(k, plain_text))


def breakTheCipher():
	cipher_text = read_file(CIPHER_TEXT_FILE)
	findPossiblePlainTexts(cipher_text)

def main():
	breakTheCipher()
	
if __name__ == '__main__':
	main()