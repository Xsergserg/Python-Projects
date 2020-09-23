def computepay(h,r):
	if h <= 40:
		return h * r
	else:
		return 40 * r + (h - 40) * 1.5 * r

hrs = input("Enter Hours:")
r = input("Enter rate:")
hrs = float(hrs)
r = float(r)
p = computepay(hrs,r)
print("Pay",p)
