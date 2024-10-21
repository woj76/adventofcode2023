#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 16

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

l = len(data[0])

# Seems I slashed the solution to part 1 here too
# part2 = False

max_x = len(data[0])
max_y = len(data)

rules = {}

rules[((1,0),'.')] = [(1,0)]
rules[((1,0),'-')] = [(1,0)]
rules[((1,0),'|')] = [(0,-1),(0,1)]
rules[((1,0),'/')] = [(0,-1)]
rules[((1,0),'\\')] = [(0,1)]
rules[((0,1),'.')] = [(0,1)]
rules[((0,1),'-')] = [(-1,0),(1,0)]
rules[((0,1),'|')] = [(0,1)]
rules[((0,1),'/')] = [(-1,0)]
rules[((0,1),'\\')] = [(1,0)]
rules[((-1,0),'.')] = [(-1,0)]
rules[((-1,0),'-')] = [(-1,0)]
rules[((-1,0),'|')] = [(0,-1),(0,1)]
rules[((-1,0),'/')] = [(0,1)]
rules[((-1,0),'\\')] = [(0,-1)]
rules[((0,-1),'.')] = [(0,-1)]
rules[((0,-1),'-')] = [(-1,0),(1,0)]
rules[((0,-1),'|')] = [(0,-1)]
rules[((0,-1),'/')] = [(1,0)]
rules[((0,-1),'\\')] = [(-1,0)]

enters = []
for x in range(1,max_x-1):
	enters.append((x,0,(0,1)))
	enters.append((x,max_y-1,(0,-1)))
for y in range(1,max_y-1):
	enters.append((0,y,(1,0)))
	enters.append((max_x-1,y,(-1,0)))

enters.append((0,0,(1,0)))
enters.append((0,0,(0,1)))
enters.append((max_x-1,0,(-1,0)))
enters.append((max_x-1,0,(0,1)))

enters.append((0,max_y-1,(1,0)))
enters.append((0,max_y-1,(0,-1)))
enters.append((max_x-1,max_y-1,(-1,0)))
enters.append((max_x-1,max_y-1,(0,-1)))

total = 0

for e in enters:
	old_visited = 0
	beams = [e]
	visited = {}
	while True:
		new_beams = []
		added = False
		for bx,by,(dx,dy) in beams:
			if (bx,by,dx,dy) in visited:
				continue
			visited[(bx,by,dx,dy)] = True
			for ndx,ndy in rules[(dx,dy),data[by][bx]]:
				nx,ny = (bx+ndx,by+ndy)
				if nx >= 0 and nx < max_x and ny >= 0 and ny < max_y:
					new_beams.append((nx,ny,(ndx,ndy)))
		if len(visited) == old_visited:
			break
		old_visited = len(visited)
		beams = new_beams

	visited2 = {}
	for bx,by,dx,dy in visited:
		visited2[(bx,by)] = True

	t = len(visited2)
	if t > total:
		total = t

print(f"Part 2: {total}")
