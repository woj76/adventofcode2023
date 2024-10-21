#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 13

input_data = get_input()

data = [x for x in input_data.split('\n\n') if x != '']

# Seems I slashed the part 1 solution
#part2 = True

def check_mirror(d):
	rrr = []
	d = [x for x in d.split('\n') if x != '']
	for c in range(1,len(d)):
		l1 = c
		l2 = len(d)-c
		if l1 > l2:
			lll = l2
		else:
			lll = l1
		mirror = True
		ll = d[c-lll:c]
		rr = d[c:c+lll][::-1]
		assert len(ll) == len(rr) and len(rr) == lll and len(ll) == lll
		for i in range(len(ll)):
			if ll[i] != rr[i]:
				mirror=False
				break
		if mirror:
			rrr.append((100,c))

	for c in range(1,len(d[0])):
		l1 = c
		l2 = len(d[0])-c
		if l1 > l2:
			lll = l2
		else:
			lll = l1
		mirror = True
		for line in d:
			ll = line[c-lll:c]
			rr = line[c:c+lll][::-1]
			if ll != rr:
				mirror=False
				break
		if mirror:
			rrr.append((1,c))
	return rrr

res = 0
for d in data:
	[(m,c)] = check_mirror(d)
	lst = []
	for i in range(len(d)):
		if d[i] == '.' or d[i] == '#':
			nd = d[0:i] + ('.' if d[i] == '#' else '#') + d[i+1:]
			rr_rr = check_mirror(nd)
			if rr_rr != [] and rr_rr not in lst and rr_rr != (m,c):
				for (m1,c1) in rr_rr:
					if (m1,c1) != (m,c) and (m1,c1) not in lst:
						lst.append((m1,c1))
	(m,c) = lst[0]
	res += m*c

print(f"Part 2: {res}")

