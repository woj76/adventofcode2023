#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 19

input_data = get_input()

[rules,items] = [x.strip() for x in input_data.split('\n\n') if x != '']

transitions = {}

for r in rules.split('\n'):
	[fr,nx] = r.split('{')
	nx = nx[:-1].split(',')
	# print(fr, nx)
	transitions[fr] = nx

its = []
for i in items.split('\n'):
	i = i[1:-1].split(',')
	k = {}
	for v in i:
		[nn,vv] = v.split('=')
		vv = int(vv)
		k[nn] = vv
	its.append(k)

def process(itm,fr):
	if fr == 'A' or fr == 'R':
		return fr
	rule = transitions[fr]
	for r in rule[:-1]:
		[cnd,t] = r.split(':')
		cn,cc,cv = cnd[0],cnd[1],int(cnd[2:])
		assert cc == '<' or cc == '>'
		if cc == '<':
			if itm[cn] < cv:
				return process(itm,t)
		elif cc == '>':
			if itm[cn] > cv:
				return process(itm,t)
	return process(itm,rule[-1])

res = 0

for i in its:
	if process(i,"in") == 'A':
		res += sum(i.values())

print(f"Part 1: {res}")

As = 0

def process2(itm,fr):
	#print(itm)
	global As, Rs
	if fr == 'A':
		rr = 1
		for a,b in itm.values():
			rr *= (b-a+1)
		As += rr
		return
	if fr == 'R':
		return
	rule = transitions[fr]
	for r in rule[:-1]:
		[cnd,t] = r.split(':')
		cn,cc,cv = cnd[0],cnd[1],int(cnd[2:])
		a,b = itm[cn]
		if cc == '<':
			if cv <= a:
				continue
			if cv > b:
				process2(itm,t)
				return
			a2,b2 = cv,b
			itm2 = {}
			for cnn,r in itm.items():
				if cnn != cn:
					itm2[cnn] = r
			itm2[cn] = (a2,b2)
			process2(itm2,fr)
			a1,b1 = a,cv-1
			itm[cn] = (a1,b1)
			process2(itm,t)
			return
		elif cc == '>':
			if cv >= b:
				continue
			if cv < a:
				process2(itm,t)
				return
			a2,b2 = a,cv
			itm2 = {}
			for cnn,r in itm.items():
				if cnn != cn:
					itm2[cnn] = r
			itm2[cn] = (a2,b2)
			process2(itm2,fr)
			a1,b1 = cv+1,b
			itm[cn] = (a1,b1)
			process2(itm,t)
			return
	process2(itm,rule[-1])

all_items = {'x':(1,4000),'a':(1,4000),'m':(1,4000),'s':(1,4000)}

process2(all_items,"in")

print(f"Part 2: {As}")

