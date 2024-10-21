#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 9

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

res = 0

for d in data:
	d = [int(x) for x in d.split(' ')]
	lasts = []
	while True:
		all_zeros = True
		new_d = []
		for i in range(1,len(d)):
			ne = d[i]-d[i-1]
			if ne != 0:
				all_zeros = False
			new_d.append(ne)
		if part2:
			lasts.append(d[0])
		else:
			lasts.append(d[-1])
		d = new_d
		if all_zeros:
			break
	if part2:
		p = 0
		for l in reversed(lasts):
			p = l - p
		res += p
	else:
		res += sum(lasts)

print(f"Part {2 if part2 else 1}: {res}")

