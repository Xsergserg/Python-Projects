largest = None
smallest = None
while True:
	usr_input = input("Enter a number: ")
	if usr_input == "done" : break
	try:
		num = int(usr_input)
	except:
		print("Invalid input")
		continue
	if not smallest or num < smallest : smallest = num
	if not largest or num > largest : largest = num
print("Maximum is", largest)
print("Minimum is", smallest)
