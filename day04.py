#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 4

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

res = 0

copies = {}
cards = {}

for d in data:
	[gid,d] = d.split(': ')
	gid = int(gid[5:].strip())
	[win,have] = d.split(' | ')
	win = [int(n.strip()) for n in win.split(' ') if n != '']
	have = [int(n.strip()) for n in have.split(' ') if n != '']
	copies[gid] = 1
	cards[gid] = (win,have)

if part2:
	for gid in cards:
		(win,have) = cards[gid]
		w = 0
		for h in have:
			if h in win:
				w += 1
		for i in range(w):
			f_gid = gid+i+1
			if f_gid in copies:
				copies[f_gid] = copies[f_gid] + copies[gid]
	for _,c in copies.items():
		res += c
else:
	for gid in cards:
		(win,have) = cards[gid]
		w = 0
		for h in have:
			if h in win:
				w = 1 if w == 0 else 2*w
		res += w

print(f"Part {2 if part2 else 1}: {res}")

