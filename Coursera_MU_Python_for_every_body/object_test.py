class test_obj:
	x = 0

	def __init__(self, x):
		self.x = x
		print("I'm here and x =", self.x)
	def inc(self):
		self.x += 1
	def __del__(self):
		print("I had gone")

test = test_obj(10)
test.inc()
print ("test.x after increment:", test.x)
