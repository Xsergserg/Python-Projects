name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()
for line in handle:
	if line.startswith('From '):
		word = line.split()
		time = word[5].split(':')
		dic[time[0]] = dic.get(time[0], 0) + 1
res = sorted(dic.items())
for k, v in res:
	print (k, v)
