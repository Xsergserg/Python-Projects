#def asci(str_in):
#	str_res = ''
#	for i in str_in:
#		if i != ' ':
#			str_res += str(ord(i)-96) + ' '
#		else:
#			str_res += '\t'
#	print str_res

#def create_phone_number(n):
#	str_res = '('
#	i = 0
#	for num in n:
#		i += 1
#		str_res += str(num)
#		if i == 3:
#			str_res += ')'
#		if i == 6:
#			str_res += '-'
#	return str_res

def chooser(n):
	if n[0] == '0':
		return ['00', n]
	else:
		return ['0', n.replace('1', '0')]

def rev_chooser (n):
	if n[0]	== '00':
		return n[1]
	else:
		return n[1].replace('0', '1')

def send(s):
	res = ''
	new_res = ''
	result = []
	for let in s:
		sym = str(bin(ord(let))[2:]).zfill(7)
		res += sym
	for i in range(len(res)):
		new_res += res[i]
		if i < (len(res)-1) and res[i] != res[i+1]:
			new_res += ' '
	res = new_res.split(' ')
	res = map(chooser, res)
	for let in res:
		for i in let:
			result.append(i)
	return ' '.join(result)

def receive(s):
	i = 0
	res = s.split(' ')
	new_res = []
	result = ''
	while i < len(res):
		new_res.append([res[i], res[i+1]])
		i+=2
	res = new_res
	new_res = []
	for i in res:
		new_res.append(rev_chooser(i))
	res = ''.join(new_res)
	i = 0
	while i+7 <= len(res):
		result += chr(int(res[i:i+7], 2))
		i+=7
	return result

print send('CC')
print receive('0 0 00 0000 0 000 00 0000 0 00')