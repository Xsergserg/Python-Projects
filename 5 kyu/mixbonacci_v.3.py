from itertools import cycle

def fibonacci():
	t1, t2 = 0, 1
	while True:
		yield t1
		t1, t2 = t2, t1 + t2

def padovan():
	t1, t2, t3 = 1, 0, 0
	while True:
		yield t1
		t1, t2, t3 = t2, t3, t1 + t2

def jacobsthal():
	t1, t2 = 0, 1
	while True:
		yield t1
		t1, t2 = t2, t1*2 + t2

def pell():
	t1, t2 = 0, 1
	while True:
		yield t1
		t1, t2 = t2, t2*2 + t1

def tribonacci():
	t1, t2, t3 = 0, 0, 1
	while True:
		yield t1
		t1, t2, t3 = t2, t3, t1 + t2 + t3

def tetranacci():
	t1, t2, t3, t4 = 0, 0, 0, 1
	while True:
		yield t1
		t1, t2, t3, t4 = t2, t3, t4, t1 + t2 + t3 + t4

def mixbonacci(pattern, length):
	result = []
	if pattern == [] or length == 0:
		return result
	nacci = {
		'fib' : fibonacci(),
		'pad' : padovan(),
		'jac' : jacobsthal(),
		'pel' : pell(),
		'tri' : tribonacci(),
		'tet' : tetranacci()
	}
	i = 0
	for patt in cycle(pattern):
		if i >= length : break
		result.append(next(nacci[patt]))
		i += 1
	return result
