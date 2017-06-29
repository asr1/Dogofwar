import sys
import math
import copy

THRESHOLD = 5 #The most amount I'm willing to go over

sheetnums = set()

num = int(sys.argv[1])
currnum = num

class option:
	leftover = 0
	tups = []
	sheets = 0
	
class sht:
	x = 0
	y = 0
	xy = x * y

	def __init__(self, newx, newy, newxy):
		self.x = newx
		self.y = newy
		self.xy = newxy
		
	def __str__(self):
		return "X: " + str(self.x) +  ", Y: " + str(self.y) + ", X * Y: " + str(self.xy)

	def __eq__(self, other):
		return int(self.xy) == int(other.xy)
	def __le__(self, other):
		return int(self.xy) <= int(other.xy)
	def __ne__(self, toher):
		return int(self.xy) != int(other.xy)
	def __lt__(self, other):
		return int(self.xy) < int(other.xy)
	def __gt__(self, other):
		return int(self.xy) > int(other.xy)
	def __ge__(self, other):
		return int(self.xy) >= int(other.xy)
	def __hash__(self):
		return int(self.xy)
		
		
for x in range(2, 11):
	for y in range(1, 8):
		sheetnums.add(sht(x, y, x*y -1))

#print(sheetnums)
print()
for i in sheetnums:
	print(i)



opts = []


run = 0

while THRESHOLD > 0:
	sheetnums2 = copy.deepcopy(sheetnums)

	#Do the business
	while run < 3:
		first = None
		remain = num + THRESHOLD
		while remain > 0:
			sub = max(opt.xy for opt in sheetnums2 if opt.xy <= remain)
			if first is None:
				for m in sheetnums2:
					#print(m)
					if m.xy == sub:
						first = m
						break
			
			
			print("First is: " + str(first))
			print("sub: " + str(sub))
			remain = remain - sub
			
			opts.append(sub)
		
		print(opts)
		opts.clear()
		print()
		run = run + 1
		sheetnums2.remove(first)
		

		#for y in sheetnums:
		#	amt = x * y
		#	remaining = num
		#	o = option()
		#	o.tups.append((x,y))
		#	for i in o.tups:
		#		print(i)


	#for x in range(0, int(math.sqrt(num) + 1)):
	#	print(x)
	THRESHOLD = THRESHOLD - 1
		

	