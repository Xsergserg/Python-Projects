
def fibonacci(num):
	i = 0
	t1, t2 = 0, 1
	while i < num:
		t1, t2 = t2, t1 + t2
		i += 1
	return t1

def padovan(num):
	i = 0
	t1, t2, t3 = 1, 0, 0
	while i < num:
		t1, t2, t3 = t2, t3, t1 + t2
		i += 1
	return t1

def jacobsthal(num):
	i = 0
	t1, t2 = 0, 1

	while i < num:
		t1, t2 = t2, t1*2 + t2
		i += 1
	return t1

def pell(num):
	i = 0
	t1, t2 = 0, 1

	while i < num:
		t1, t2 = t2, t2*2 + t1
		i += 1
	return t1

def tribonacci(num):
	i = 0
	t1, t2, t3 = 0, 0, 1

	while i < num:
		t1, t2, t3 = t2, t3, t1 + t2 + t3
		i += 1
	return t1

def tetranacci(num):
	i = 0
	t1, t2, t3, t4 = 0, 0, 0, 1
	while i < num:
		t1, t2, t3, t4 = t2, t3, t4, t1 + t2 + t3 + t4
		i += 1
	return t1

def mixbonacci(pattern, length):
	result = []
	if pattern == [] or length == 0:
		return result
	nacci = {
		'fib' : 0,
		'pad' : 0,
		'jac' : 0,
		'pel' : 0,
		'tri' : 0,
		'tet' : 0
	}
	i = 0
	while i < length:
		for patt in pattern:
			if i >= length : break
			if patt == 'fib': result.append(fibonacci(nacci[patt]))
			if patt == 'pad': result.append(padovan(nacci[patt]))
			if patt == 'jac': result.append(jacobsthal(nacci[patt]))
			if patt == 'pel': result.append(pell(nacci[patt]))
			if patt == 'tri': result.append(tribonacci(nacci[patt]))
			if patt == 'tet': result.append(tetranacci(nacci[patt]))
			nacci[patt] += 1
			i += 1
	return result

print (mixbonacci(['jac', 'jac', 'pel'], 10))
