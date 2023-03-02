import base64

def crypto(target):
	return base64.b64encode(target.encode('utf-8'))
def decrypto(target):
	return base64.b64decode(target).decode('utf-8')

while True:
	a = input('--> ')
	print(crypto(a))