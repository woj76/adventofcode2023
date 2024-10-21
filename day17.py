#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 17

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

max_x = len(data[0])
max_y = len(data)

if part2:
	steps = [4,5,6,7,8,9,10]
else:
	steps = [1,2,3]

def n(x,y,l):
	r = []
	if l != 'l' and l != 'r':
		c = 0
		for i in range(1,steps[0]):
			if x+i < max_x:
				c += int(data[y][x+i])
		for i in steps:
			if x+i < max_x:
				c += int(data[y][x+i])
				r.append((x+i,y,'r',c))
		c = 0
		for i in range(1,steps[0]):
			if x-i >= 0:
				c += int(data[y][x-i])
		for i in steps:
			if x-i >= 0:
				c += int(data[y][x-i])
				r.append((x-i,y,'l',c))
	if l != 'u' and l != 'd':
		c = 0
		for i in range(1,steps[0]):
			if y+i < max_y:
				c += int(data[y+i][x])
		for i in steps:
			if y+i < max_y:
				c += int(data[y+i][x])
				r.append((x,y+i,'d',c))
		c = 0
		for i in range(1,steps[0]):
			if y-i >= 0:
				c += int(data[y-i][x])
		for i in steps:
			if y-i >= 0:
				c += int(data[y-i][x])
				r.append((x,y-i,'u',c))
	return r

import heapq
from collections import defaultdict

visited = set()
q = []
dist = defaultdict(lambda : float('inf'))

S = (0,0,'x')
E = (max_x-1,max_y-1)

dist[S] = 0
heapq.heappush(q, (0, S))

while q:
	_, u = heapq.heappop(q)
	for vx,vy,vd,vc in n(u[0],u[1],u[2]):
		v = (vx,vy,vd)
		alt = dist[u] + vc
		if alt < dist[v]:
			dist[v] = alt
			heapq.heappush(q, (alt, v))

min_dist = float('inf')

for v in dist:
	if (v[0],v[1]) == E:
		if dist[v] < min_dist:
			min_dist = dist[v]

print(f"Part {2 if part2 else 1}: {min_dist}")

