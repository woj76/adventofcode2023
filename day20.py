#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 20

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

gates = {}

for d in data:
	[f,t] = d.split(' -> ')
	if f[0] == '%':
		gates[f[1:]] = ('f',t.split(', '))
	elif f[0] == '&':
		gates[f[1:]] = ('c',t.split(', '))
	else:
		gates[f] = ('b',t.split(', '))

states = {}

def init_states():
	for n,(t,cs) in gates.items():
		if t == 'f':
			states[n] = 0
		if t == 'c':
			s = {}
			for n1,(_,cs1) in gates.items():
				if n in cs1:
					s[n1] = 0
			states[n] = s
# gates['button'] = ('b',['broadcaster'])

init_states()

def pulse(ps):
	new_pulses = []
	for t,(s,lv) in ps:
		if t not in gates:
			continue
		g = gates[t]
		if g[0] == 'b':
			for ds in g[1]:
				new_pulses.append((ds,(t,lv)))
			continue
		gs = states[t]
		if g[0] == 'f':
			if lv == 1:
				continue
			states[t] = 0 if gs == 1 else 1
			for ds in g[1]:
				new_pulses.append((ds,(t,states[t])))
			continue
		if g[0] == 'c':
			gs[s] = lv
			all_high = 0
			for x in gs.values():
				if x == 0:
					all_high = 1
					break
			for ds in g[1]:
				new_pulses.append((ds,(t,all_high)))
	return new_pulses

highs = 0
lows = 0

for _ in range(1000):
	p = [('broadcaster',('button',0))]
	while p:
		for x,(y,lv) in p:
			if lv == 1:
				highs += 1
			else:
				lows += 1
		p = pulse(p)

print(f"Part 1: {highs*lows}")

init_states()

xxx = {}
presses = 0
while True:
	p = [('broadcaster',('button',0))]
	presses += 1
	while p:
		rx_found = False
		for x,(y,lv) in p:
			if x == 'rx' and lv == 0:
				rx_found = True
				break
		if rx_found:
			break
		p = pulse(p)
		st = False
		for n,v in states['nc'].items():
			if v == 1:
				if n not in xxx:
					xxx[n] = presses
					if len(xxx) == 4:
						r = 1
						for yyy in xxx.values():
							r *= yyy
						print(f"Part 2: {r}")
						st = True
						exit(0)
				else:
					pr = presses-xxx[n]
					if pr != 0:
						st = True
						xxx[n] = pr
		if st:
			break
