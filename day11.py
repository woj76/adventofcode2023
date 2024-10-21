#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 11

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

res = 0

galaxies = {}
empty_rows = []
empty_rows_num = 0
empty_cols = []
empty_cols_num = 0

for y in range(len(data)):
	all_dot = True
	for x in range(len(data[y])):
		if data[y][x] == '#':
			galaxies[(x,y)] = '#'
			all_dot = False
	if all_dot:
		empty_rows_num += ((1000000-1) if part2 else 1)
	empty_rows.append(empty_rows_num)

for x in range(len(data[0])):
	all_dot = True
	for y in range(len(data)):
		if data[y][x] != '.':
			all_dot = False
	if all_dot:
		empty_cols_num += ((1000000-1) if part2 else 1)
	empty_cols.append(empty_cols_num)

gals = [x for x in galaxies]

res = 0

for i in range(len(gals)):
	for j in range(i+1,len(gals)):
		g1x,g1y = gals[i]
		g2x,g2y = gals[j]
		g1x += empty_cols[g1x]
		g2x += empty_cols[g2x]
		g1y += empty_rows[g1y]
		g2y += empty_rows[g2y]
		d = int(abs(g1x-g2x)+abs(g1y-g2y))
		res += d

print(f"Part {2 if part2 else 1}: {res}")

