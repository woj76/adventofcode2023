#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 3

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

res = 0
part_markers = {}
part_numbers = {}
for y,d in enumerate(data):
	x = 0
	while x < len(d):
		if d[x].isdigit():
			i = 0
			while d[x:x+i+1].isdigit() and x+i < len(d):
				i += 1
			part_numbers[(x,y)] = d[x:x+i]
			x += i
		else:
			if d[x] != '.':
				part_markers[(x,y)] = d[x]
			x += 1

if part2:
	for (i,j),m in part_markers.items():
		if m != '*':
			continue
		ratio = 1
		count = 0
		for (x,y),part_name in part_numbers.items():
			if i in range(x-1,x+len(part_name)+1) and j in range(y-1,y+2):
				count += 1
				ratio *= int(part_name)
		if count > 1:
			res += ratio
else:
	for (x,y),part_name in part_numbers.items():
		for i in range(x-1,x+len(part_name)+1):
			for j in range(y-1,y+2):
				if (i,j) in part_markers:
					res += int(part_name)

print(f"Part {2 if part2 else 1}: {res}")

