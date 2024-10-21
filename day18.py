#!/usr/bin/pypy3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 18

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

bx,by = 0,0

dirs = {'R':(1,0),'0':(1,0),'L':(-1,0),'2':(-1,0),'U':(0,-1),'3':(0,-1),'D':(0,1),'1':(0,1)}

min_x = bx
max_x = bx

hlines = {}
vlines = {}

for d in data:
	[d,s,c] = d.split(' ')
	if part2:
		c = c[2:-1]
		s = int(c[:-1],16)
		d = c[-1]
	else:
		s = int(s)
	dtx,dty = dirs[d]
	ex = bx+s*dtx
	ey = by+s*dty
	min_x = min(min_x,bx)
	max_x = max(max_x,bx)
	min_x = min(min_x,ex)
	max_x = max(max_x,ex)

	if bx == ex:
		if by < ey:
			vlines[(bx,by,ey)] = True
		else:
			vlines[(bx,ey,by)] = True
	if by == ey:
		if bx < ex:
			hlines[(by,bx,ex)] = True
		else:
			hlines[(by,ex,bx)] = True
	bx = ex
	by = ey

area = 0

total = max_x-min_x
cnt = 0
for x in range(min_x,max_x+1):
	cnt += 1
	if cnt % 10000 == 0:
		print(cnt, total)
	selected_hlines = sorted([l for l in hlines if x>=l[1] and x<=l[2]])
	sl = len(selected_hlines)
	i = 0
	odd = 0
	while i<sl-1:
		curr_hline1 = selected_hlines[i]
		curr_hline2 = selected_hlines[i+1]
		selected_vlines_opposite = [l for l in vlines if x == l[0] and ((l[1] == curr_hline1[0] and l[2] == curr_hline2[0]) and ((x == curr_hline1[1] and x == curr_hline2[2]) or (x == curr_hline1[2] and x == curr_hline2[1])))]
		if len(selected_vlines_opposite) == 1:
			area += (selected_vlines_opposite[0][2]-selected_vlines_opposite[0][1])
			i += 1
			odd = 1 if odd == 0 else 0
			continue
		if i % 2 == odd:
			area += curr_hline2[0]-curr_hline1[0]+1
		else:
			selected_vlines_same = [l for l in vlines if x == l[0] and ((l[1] == curr_hline1[0] and l[2] == curr_hline2[0]) and ((x == curr_hline1[1] and x == curr_hline2[1]) or (x == curr_hline1[2] and x == curr_hline2[2])))]
			if len(selected_vlines_same) == 1:
				area += (selected_vlines_same[0][2]-selected_vlines_same[0][1]-1)
		i += 1

print(f"Part {2 if part2 else 1}: {area}")

