#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 15


input_data = get_input()

data = [x for x in input_data.strip().split(',')]

def h(s,curr):
	for c in s:
		c = ord(c)
		curr += c
		curr *= 17
		curr %= 256
	return curr

res = 0
curr = 0
for ss in data:
	curr = h(ss,0)
	res += curr

print(f"Part 1: {res}")

boxes = {}
for i in range(256):
	boxes[i] = []

for ss in data:
	if '-' in ss:
		[id,_a] = ss.split('-')
		assert _a == ""
		n = h(id,0)
		boxes[n] = [(e,x) for e,x in boxes[n] if e != id]
	elif '=' in ss:
		[id,a] = ss.split('=')
		a = int(a)
		n = h(id,0)
		present = False
		for e,x in boxes[n]:
			if e == id:
				present = True
				break
		if present:
			boxes[n] = [(e,x if e != id else a) for e,x in boxes[n]]
		else:
			boxes[n].append((id,a))

res = 0
for b in boxes:
	for i,(e,x) in enumerate(boxes[b]):
		res += (b+1)*(i+1)*x

print(f"Part 2: {res}")

