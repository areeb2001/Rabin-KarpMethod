alp = 256
def search(pat, txt, primeNum):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 # hash value for pattern
	t = 0 # hash value for txt
	h = 1
	# The value of h would be "pow(d, M-1)% q"
	for i in range(M-1):
		h = (h * alp)% primeNum

	for i in range(M):
		p = (alp * p + ord(pat[i]))% primeNum
		t = (alp * t + ord(txt[i]))% primeNum

	for i in range(N-M + 1):
		if p == t:
			# Check for characters one by one
			for j in range(M):
				if txt[i + j] != pat[j]:
					break

			j+= 1
			if j == M:
				print ("Pattern found at index " + str(i))
		if i < N-M:
			t = (alp*(t-ord(txt[i])*h) + ord(txt[i + M]))% primeNum
			if t < 0:
				t = t + primeNum

txt =input("Enter Value")
pat =input("Enter pattern")
primeNum = 101
search(pat, txt, primeNum)