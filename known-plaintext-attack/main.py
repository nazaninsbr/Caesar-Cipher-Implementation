PLAIN_TEXT_FILE = './plain_text.txt'
CIPHER_TEXT_FILE = './cipher_text.txt'

def read_file(path):
	content = []
	with open(path, 'r') as f:
		for line in f:
			content.append(line)
	return content

def findTheKey(plain_text, cipher_text):
	i = 0
	j = 0
	key = 0
	while True:
		if plain_text[i][j]==' ':
			j += 1
			continue
		if j>= len(plain_text[i]):
			j = 0
			i += 1
			continue
		if i >= len(plain_text):
			print('Couldn\'t find the key:(')
			exit()
		key = ord(cipher_text[i][j])-ord(plain_text[i][j])
		break
	return key

def breakTheCipher():
	plain_text = read_file(PLAIN_TEXT_FILE)
	cipher_text = read_file(CIPHER_TEXT_FILE)
	key = findTheKey(plain_text, cipher_text)
	print('The key is: ', key)

def main():
	breakTheCipher()
	
if __name__ == '__main__':
	main()