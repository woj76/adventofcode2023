#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 2

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

res = 0
for d in data:
	g,c = d.split(': ')
	gid = int(g.split(' ')[1])
	c = c.split('; ')
	possible = True
	if part2:
		min_draws = {'red' : 0, 'green' : 0, 'blue' : 0}
	for rgb in c:
		draw = {'red' : 0, 'green' : 0, 'blue' : 0}
		for b in rgb.split(', '):
			bb = b.split(' ')
			draw[bb[1]] = int(bb[0])
		if part2:
			for clr in min_draws:
				if draw[clr] > min_draws[clr]:
					min_draws[clr] = draw[clr]
		else:
			if draw['red'] > 12 or draw['green'] > 13 or draw['blue'] > 14:
				possible = False
				break
	if part2:
		res += (min_draws['red'] * min_draws['green'] * min_draws['blue'])
	else:
		if possible:
			res += gid

print(f"Part {2 if part2 else 1}: {res}")

