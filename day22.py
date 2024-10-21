#!/usr/bin/pypy3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 22

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

res = 0

space = {}
org_bricks = []

for d in data:
	d = d.split("~")
	b1 = tuple([int(c) for c in d[0].split(',')])
	b2 = tuple([int(c) for c in d[1].split(',')])
	org_bricks.append((b1,b2))

def can_fall(bricks, brick_index, excl):
	b1,b2 = bricks[brick_index]
	can_fall = True
	if b1[2] == 1:
		can_fall = False
	else:
		for j in range(len(bricks)):
			if j == brick_index or j == excl:
				continue
			bb1,bb2 = bricks[j]
			for x in range(b1[0],b2[0]+1):
				for y in range(b1[1],b2[1]+1):
					if bb1[0] <= x <= bb2[0] and bb1[1] <= y <= bb2[1] and bb2[2] == b1[2]-1:
						can_fall = False
						break
				if not can_fall:
					break
			if not can_fall:
				break
	return can_fall

moved = True
while moved:
	moved = False
	for i in range(len(org_bricks)):
		b1,b2 = org_bricks[i]
		if can_fall(org_bricks, i, -1):
			moved = True
			org_bricks[i] = ((b1[0],b1[1],b1[2]-1),(b2[0],b2[1],b2[2]-1))

falling_bricks = []

for i in range(len(org_bricks)):
	cf = False
	for j in range(len(org_bricks)):
		if i == j:
			continue
		if can_fall(org_bricks,j,i):
			cf = True
			break
	if not cf:
		res += 1
	else:
		falling_bricks.append(i)

print(f"Part 1: {res}")

res = 0

for j in falling_bricks:
	new_bricks = org_bricks.copy()
	fallen = {}
	moved = True
	while moved:
		moved = False
		for i in range(len(new_bricks)):
			b1,b2 = new_bricks[i]
			if can_fall(new_bricks, i, j):
				moved = True
				new_bricks[i] = ((b1[0],b1[1],b1[2]-1),(b2[0],b2[1],b2[2]-1))
				fallen[i] = True
	res += len(fallen)

print(f"Part 2: {res}")
