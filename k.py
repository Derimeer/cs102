def encrypt_caesar(plaintext):
	"""
	>>> encrypt_caesar("python")
	'sbwkrq'
	"""
	ciphertext = ""
	for c in plaintext:
		x = ord(c)
		if x == ord('Z') or x == ord('Y') or \
			x == ord('X') or x == ord('z') or \
			x == ord('y') or x == ord('x'):
				i = x-23
				p = chr(i)
				ciphertext += p
		elif x == ord('Я') or x == ord('я') or \
			x == ord('э') or x == ord('Э') or \
			x == ord('Ю') or x == ord('ю'):
				c = x-30
				p = chr(c)
				ciphertext += p
		else:
			i = x-3
			p = chr(i)
			ciphertext += p
	return ciphertext
