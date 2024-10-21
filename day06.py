#!/usr/bin/python3

year = 2023
day = 6

from math import sqrt

times = [48,98,90,83]
distances = [390,1103,1112,1360]

res = 1

for i in range(len(times)):
	t = times[i]
	d = distances[i]
	w = 0
	for p in range(t):
		md = (t-p)*p
		if md > d:
			w += 1
	res *= w
print(f"Part 1: {res}")

time = 48989083
distance = 390110311121360

delta = sqrt(time*time-4*distance)
solution1 = (time-delta)/2
solution2 = (time+delta)/2

print(f"Part 2: {int(solution2) - int(solution1)}")
