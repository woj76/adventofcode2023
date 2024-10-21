#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 14

input_data = get_input()

data = [list(x) for x in input_data.split('\n') if x != '']

part2 = True

def tilt_north():
	for y in range(1,len(data)):
		for x in range(len(data[y])):
			if data[y][x] == 'O':
				j = y-1
				while j>=0 and data[j][x] == '.':
					j -= 1
				j += 1
				if j != y:
					data[j][x] = 'O'
					data[y][x] = '.'

def tilt_east():
	for x in range(len(data[0])-2,-1,-1):
		for y in range(len(data)):
			if data[y][x] == 'O':
				i = x+1
				while i<len(data[y]) and data[y][i] == '.':
					i += 1
				i -= 1
				if i != x:
					data[y][i] = 'O'
					data[y][x] = '.'

def tilt_south():
	for y in range(len(data)-2,-1,-1):
		for x in range(len(data[y])):
			if data[y][x] == 'O':
				j = y+1
				while j<len(data) and data[j][x] == '.':
					j += 1
				j -= 1
				if j != y:
					data[j][x] = 'O'
					data[y][x] = '.'

def tilt_west():
	for x in range(1,len(data[0])):
		for y in range(len(data)):
			if data[y][x] == 'O':
				i = x-1
				while i>=0 and data[y][i] == '.':
					i -= 1
				i += 1
				if i != x:
					data[y][i] = 'O'
					data[y][x] = '.'


res = 0

def st():
	return "".join(["".join(l) for l in data])

first = st()

# The solution to part 2 was guessed out of these repeating values

"""140 79742
141 79734
142 79723
143 79716
144 79708
145 79714
146 79711
147 79708
148 79718
149 79724
150 79727
151 79731
152 79718
153 79723
154 79730
155 79736
156 79733
157 79743
"""

if part2:
	for i in range(1000000000):
		if i % 1000 == 0:
			print(i)
		tilt_north()
		tilt_west()
		tilt_south()
		tilt_east()
		#if st() == first:
		#	print(i)
		#	break
		res = 0
		w = 1
		for l in data[::-1]:
			res += l.count('O')*w
			w += 1
		print(i, res)
		if i == 500:
			break
else:
	tilt_north()

res = 0
w = 1
for l in data[::-1]:
	res += l.count('O')*w
	w += 1


print(res)

