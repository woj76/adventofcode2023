#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 8

input_data = get_input()

data = [x for x in input_data.split('\n\n') if x != '']

part2 = True

res = 0

directions = data[0].strip()

tree = {}

for d in data[1].split('\n'):
	if d == '':
		break
	[s,dd] = d.split(' = ')
	[dd1,dd2] = dd.split(', ')
	dd1 = dd1[1:]
	dd2 = dd2[:-1]
	tree[s] = (dd1,dd2)

if part2:
	start_node = []
	for n in tree:
		if n[-1] == 'A':
			start_node.append(n)
else:
    start_node = ["AAA"]

cc = []

for sn in start_node:
	i = 0
	res = 0
	while True:
		ind = 0 if directions[i] == 'L' else 1
		res += 1
		i = (i+1) % len(directions)
		sn = tree[sn][ind]
		if (part2 and sn[-1] == 'Z') or (not part2 and sn == 'ZZZ'):
			break
	cc.append(res)

from math import gcd

g = cc[0]
lcm = g

for c in cc[1:]:
	g = gcd(g,c)
	lcm = (lcm * c) // g

print(f"Part {2 if part2 else 1}: {lcm}")

