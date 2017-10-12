def encrypt_vigenere(plaintext, keyword1):
	"""
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
	keyword1 = ''
	while len(a) > len(keyword1):
		keyword1 += b
	keyword1 = keyword1[:len(a):]
	t = len(a)
	plaintext = ''
	for c in range(t):
		o = a[c]
		x = ord(o)
		if (x > 64) and (x < 91):
			y = keyword1[c]
			s = ord(y)
			i = s - 65
			m = i+x
			if m > 90:
				n = m - 26
				p = chr(n)
				plaintext += p
			else:
				p = chr(m)
				plaintext += p
		elif (x > 96) and (x < 123):
			y = keyword1[c]
			s = ord(y)
			i = s - 95
			m = i+x
			if m > 122:
				n = m - 26
				p = chr(n)
				plaintext += p
			else:
				p = chr(m)
				plaintext += p
		elif (x > 1039) and (x < 1072):
			y = keyword1[c]
			s = ord(y)
			i = s - 1040
			m = i+x
			if m > 1071:
				n = m - 33
				p = chr(n)
				plaintext += p
			else:
				p = chr(m)
				plaintext += p
		else:
			y = keyword1[c]
			s = ord(y)
			i = s - 1072
			m = i+x
			if m > 1103:
				n = m - 33
				p = chr(n)
				plaintext += p
			else:
				p = chr(m)
				plaintext += p
	return ciphertext
