#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 1

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = os.path.exists(f"day{day}level1.txt")

part2 = True

if part2:
	digits = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
else:
	digits = {}

for i in [1,2,3,4,5,6,7,8,9]:
	digits[str(i)] = i

res = 0
for d in data:
	i0,i1 = float('inf'),float('-inf')
	d0 = d1 = 0
	for dd in digits:
		for i in range(len(d)):
			if d[i:i+len(dd)] == dd:
				if i < i0:
					d0 = digits[dd]
					i0 = i
				if i > i1:
					d1 = digits[dd]
					i1 = i
	n = d0*10+d1
	res += n

print(f"Part {2 if part2 else 1}: {res}")

