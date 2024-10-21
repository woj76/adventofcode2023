#!/usr/bin/pypy3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 23

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

max_y = len(data)
max_x = len(data[0])

start = (1,0)
end = (max_x-2,max_y-1)

#part2 = True

def n(x,y):
	r = []
	if data[y][x+1] == '.' or data[y][x+1] == '>':
		r.append((x+1,y))
	if data[y][x-1] == '.' or data[y][x-1] == '<':
		r.append((x-1,y))
	if data[y+1][x] == '.' or data[y+1][x] == 'v':
		r.append((x,y+1))
	if y > 0 and (data[y-1][x] == '.' or data[y-1][x] == '^'):
		r.append((x,y-1))
	return r

def n2(x,y):
	r = []
	if y-1 >= 0 and data[y-1][x] != '#':
		r.append((x,y-1))
	if x+1 < len(data[y]) and data[y][x+1] != '#':
		r.append((x+1,y))
	if y+1 < len(data) and data[y+1][x] != '#':
		r.append((x,y+1))
	if x-1 >= 0 and data[y][x-1] != '#':
		r.append((x-1,y))
	return r

import sys
sys.setrecursionlimit(100000)

def search(path,x,y):
	global max_len
	if y == max_y-1:
		return len(path)
	m = 0
	path[(x,y)] = True
	nl = [x for x in n(x,y) if x not in path]
	for nx,ny in nl:
		mp = search(path.copy(), nx, ny)
		m = max(m, mp)
	return m

res = search({},start[0],start[1])

print(f"Part 1: {res}")

graph = {}

graph[start] = []
graph[end] = []

for y in range(1,max_y-1):
	for x in range(1,max_x):
		if data[y][x] == '.' and len(n2(x,y)) > 2:
			graph[(x,y)] = []

for vx,vy in graph:
	for nx,ny in n2(vx,vy):
		p = {(vx,vy):True, (nx,ny):True}
		sx,sy = nx,ny
		while True:
			nl = [v for v in n2(sx,sy) if v not in p]
			if len(nl) == 1:
				sx,sy = nl[0]
				p[(sx,sy)] = True
			else:
				graph[(vx,vy)].append((sx,sy,len(p)-1))
				break

def search2(path,ll,pp):
	global max_len
	if pp == end:
		return False, ll
	m = 0
	path[pp] = True
	nl = [(x1,y1,d1) for x1,y1,d1 in graph[pp] if (x1,y1) not in path]
	br = len(nl) > 1
	for nx,ny,dd in nl:
		brr,mp = search2(path.copy(), ll+dd, (nx, ny))
		m = max(m, mp)
		br = br or brr
		if not brr and mp > 0:
			break
	return br, m

_,res = search2({},0,start)

print(f"Part 2: {res}")
