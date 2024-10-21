#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 24

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

res = 0

for i in range(len(data)):
	dd = data[i]
	dd = dd.split(' @ ')
	xa,ya,za = tuple([int(x) for x in dd[0].split(', ')])
	xv,yv,zv = tuple([int(x) for x in dd[1].split(', ')])
	for j in range(i+1,len(data)):
		ddd = data[j]
		ddd = ddd.split(' @ ')
		xxa,yya,zza = tuple([int(x) for x in ddd[0].split(', ')])
		xxv,yyv,zzv = tuple([int(x) for x in ddd[1].split(', ')])
		a = yv
		b = -xv
		c = yv*xa-xv*ya
		d = yyv
		e = -xxv
		f = yyv*xxa-xxv*yya
		det = a*e-b*d
		if det == 0:
			continue
		ix = (c*e-b*f)/det
		iy = (f*a-c*d)/det
		if (ix > xa if xv > 0 else ix < xa) and (ix > xxa if xxv > 0 else ix < xxa):
			if 200000000000000 <= ix <= 400000000000000 and 200000000000000 <= iy <= 400000000000000:
			#if 7 <= ix <= 27 and 7 <= iy <= 27:
				res += 1

print(f"Part 1: {res}")

# Right, so part 2 apparently has a "simple" solutions in the form of a few
# linear equations, the required equation transformations though are just asking
# to get something wrong on the way, so it is a good occassion to try out Z3:

from z3 import *

rx, ry, rz = Ints('rx ry rz')
vrx, vry, vrz = Ints('vrx vry vrz')

s = Solver()

for i in range(len(data)):
	dd = data[i].split(' @ ')
	xa,ya,za = tuple([int(x) for x in dd[0].split(', ')])
	xv,yv,zv = tuple([int(x) for x in dd[1].split(', ')])
	k = Int('k'+str(i))
	s.add(rx + k*vrx == xa + k*xv, ry + k*vry == ya + k*yv, rz + k*vrz == za + k*zv)

res = None
if s.check() == sat:
	m = s.model()
	res = m[rx].as_long()+m[ry].as_long()+m[rz].as_long()

print(f"Part 2: {res}")

# repres(res)
