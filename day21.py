#!/usr/bin/pypy3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 21

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']
garden = {}
grass = {}

max_y = len(data)
max_x = len(data[0])
for y in range(max_y):
	for x in range(max_x):
		if data[y][x] == 'S':
			start = (x,y)
			garden[(x,y)] = '.'
			grass[(x,y)] = True
		else:
			garden[(x,y)] = data[y][x]
			if data[y][x] == '.':
				grass[(x,y)] = True

def n(pd,pr):
	r = []
	xd,yd = pd
	xr,yr = pr
	if xr+1 == max_x:
		r.append(((xd+1,yd),(0,yr)))
	else:
		r.append(((xd,yd),(xr+1,yr)))
	if xr-1 == -1:
		r.append(((xd-1,yd),(max_x-1,yr)))
	else:
		r.append(((xd,yd),(xr-1,yr)))
	if yr+1 == max_y:
		r.append(((xd,yd+1),(xr,0)))
	else:
		r.append(((xd,yd),(xr,yr+1)))
	if yr-1 == -1:
		r.append(((xd,yd-1),(xr,max_y-1)))
	else:
		r.append(((xd,yd),(xr,yr-1)))
	return r

next_round = {((0,0),start):True}

# 26501365 = 481843×5×11

all_steps = 481843*5*11

xs = []
i = 0
max_steps = 131*3+65
while i < max_steps:
	new_next_round = {}
	for d,p in next_round:
		for nd,nr in n(d,p):
			if garden[nr] == '.':
				new_next_round[(nd,nr)] = True
	next_round = new_next_round
	i += 1
	if i == 64 or i == 131+65 or i == 131*2+65 or i == 131*3+65:
		xs.append(len(next_round))

a = (xs[3]-2*xs[2]+xs[1]) / 2
c = xs[3]-3*(xs[2]-xs[1])
b = xs[1] - a - c

r = (all_steps - 65)/131

res = a*r*r + b*r + c

print(f"Part 2: {res}")
