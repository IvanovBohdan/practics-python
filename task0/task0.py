import random
a = []
for i in range(30):
	a.extend(random.randint(-100,100))
print(a)
value = max(a)
index = a.index(value)
print('Max element:', value, 'Index:', index)
for i in range(len(a)):
	if i < len(a)-1:
		if a[i] < 0 and a[i+1] < 0:
			print(a[i],a[i+1])

