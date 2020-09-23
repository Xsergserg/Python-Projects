'''
This is the first of my "-nacci" series. If you like this kata, check out the zozonacci sequence too.

Task
Mix -nacci sequences using a given pattern p.
Return the first n elements of the mixed sequence.
Rules
The pattern p is given as a list of strings (or array of symbols in Ruby) using the pattern mapping below (e. g. ['fib', 'pad', 'pel'] means take the next fibonacci, then the next padovan, then the next pell number and so on).
When n is 0 or p is empty return an empty list.
If n is more than the length of p repeat the pattern.
'''
def fibonacci(num):
	result = 0
	i = 1
	n1 = 0
	n2 = 1
	while i < num:
		result = n1 + n2
		n1 = n2
		n2 = result
		i += 1
	return 1 if num == 1 else result

def padovan(num):
	if num == 0 : return 1
	if num == 1 or num == 2: return 0
	i = 3
	t1 = 1
	t2 = 0
	t3 = 0
	while i <= num:
		result = t1 + t2
		t1 = t2
		t2 = t3
		t3 = result
		i += 1
	return result

def jacobsthal(num):
	if num == 0 : return 0
	if num == 1 : return 1
	i = 2
	t1 = 0
	t2 = 1
	while i <= num:
		result = t1*2 + t2
		t1 = t2
		t2 = result
		i += 1
	return result

def pell(num):
	if num == 0 : return 0
	if num == 1 : return 1
	i = 2
	t1 = 0
	t2 = 1
	while i <= num:
		result = t1 + t2*2
		t1 = t2
		t2 = result
		i += 1
	return result

def tribonacci(num):
	if num == 0 or num == 1: return 0
	if num == 2: return 1
	i = 3
	t1 = 0
	t2 = 0
	t3 = 1
	while i <= num:
		result = t1 + t2 + t3
		t1 = t2
		t2 = t3
		t3 = result
		i += 1
	return result

def tetranacci(num):
	if num == 0 or num == 1 or num == 2 : return 0
	if num == 3 : return 1
	i = 4
	t1 = 0
	t2 = 0
	t3 = 0
	t4 = 1
	while i <= num:
		result = t1 + t2 + t3 + t4
		t1 = t2
		t2 = t3
		t3 = t4
		t4 = result
		i += 1
	return result

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
