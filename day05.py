#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 5

input_data = get_input()

data = [x for x in input_data.split('\n\n') if x != '']

seeds = [int(x) for x in data[0][7:].split(' ')]
data = data[1:]
maps = []

for d in data:
	d = d.split('\n')[1:]
	m = []
	for l in d:
		if l == "":
			break
		(a,b,c) = tuple([int(x) for x in l.split(' ')])
		m.append((b,b+c,a-b))
	m.sort()
	maps.append(m)

res = float('inf')

ii = 0
while ii < len(seeds):
	s = seeds[ii]
	for map in maps:
		for (b,e,shift) in map:
				if s>=b and s<e:
					s += shift
					break
	if s<res:
		res = s
	ii += 1

print(f"Part 1: {res}")

res = float('inf')

ii = 0
while ii < len(seeds):
	sb = seeds[ii]
	se = sb+seeds[ii+1]
	current_ranges = [(sb,se)]
	for map in maps:
		ranges = [(float('-inf'),map[0][0])]
		ranges.append((map[0][0],map[0][1]))
		for i in range(1,len(map)):
			if map[i][0] > map[i-1][1]:
				ranges.append((map[i-1][1],map[i][0]))
			ranges.append((map[i][0],map[i][1]))
		ranges.append((map[len(map)-1][1],float('inf')))
		new_current_ranges = []
		for sb,se in current_ranges:
			new_ranges = []
			j = 0
			while j<len(ranges):
				if sb >= ranges[j][0] and sb < ranges[j][1]:
					new_ranges.append((sb,ranges[j][1]))
					break
				j+=1
			j += 1
			while j<len(ranges):
				if se < ranges[j][1]:
					new_ranges.append((ranges[j][0],se))
					break
				else:
					new_ranges.append(ranges[j])
				j += 1
			found = False
			for nrb,nre in new_ranges:
				for (b,e,shift) in map:
					if nrb>=b and nre<=e:
						new_current_ranges.append((nrb+shift,nre+shift))
						found = True
						break
				if not found:
					new_current_ranges.append((nrb,nre))
		current_ranges = new_current_ranges
	for s in current_ranges:
		if s[0] < res:
			res = s[0]
	ii += 2

print(f"Part 2: {res}")
