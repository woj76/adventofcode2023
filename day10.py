#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 10

input_data = get_input()


data = [x for x in input_data.split('\n') if x != '']

part2 = True

pipes = {}


vc = {}

vc['|'] = ('|F7','','|LJ','')
vc['-'] = ('','-J7','','-LF')
vc['F'] = ('','-J7','|LJ','')
vc['7'] = ('','','|LJ','-LF')
vc['J'] = ('|F7','','','-LF')
vc['L'] = ('|F7','-J7','','')

for y in range(len(data)):
	for x in range(len(data[y])):
		if data[y][x] == 'S':
			sx = x
			sy = y
			px = x-1
			py = y
			pipes[(x,y)] = 'J' # '7'
		else:
			pipes[(x,y)] = data[y][x]

n = [(0,-1),(1,0),(0,1),(-1,0)]

x,y = sx,sy

p = [(x,y)]

while True:
	for i in range(len(n)):
		nx,ny = x+n[i][0],y+n[i][1]
		if nx == px and ny == py:
			continue
		v = vc[pipes[(x,y)]]
		if (nx,ny) in pipes and pipes[(nx,ny)] in v[i]:
			px = x
			py = y
			x = nx
			y = ny
			break
	if x == sx and y == sy:
		break
	else:
		p.append((x,y))

print(f"Part 1: {len(p) // 2}")

res = 0

opo = {'L':'7', 'F':'J'}

for y in range(len(data)):
	isin = False
	x = 0
	while x < len(data[y]):
		if (x,y) in p:
			pp = pipes[(x,y)]
			if pp == '|':
				isin = not isin
				x += 1
				continue
			assert pp == 'F' or pp == 'L'
			x += 1
			while pipes[(x,y)] == '-':
				x += 1
			ppp = pipes[(x,y)]
			assert ppp == '7' or ppp == 'J'
			if pipes[(x,y)] == opo[pp]:
				isin = not isin
				x += 1
				continue
		elif isin:
			res += 1
		x += 1

print(f"Part 2: {res}")
