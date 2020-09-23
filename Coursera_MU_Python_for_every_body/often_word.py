name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()
name = None
count = None
for line in handle:
	if line.startswith('From '):
		x = line.split()
		dic[x[1]] = dic.get(x[1], 0) + 1
for k in dic:
	if count is None or count < dic[k]:
		name = k
		count = dic[k]
print (name, dic[name])
