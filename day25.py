#!/usr/bin/pypy3

import random

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 25

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

res = 0

# This is Karger's algorithm, see here: https://www.cs.princeton.edu/courses/archive/fall13/cos521/lecnotes/lec2final.pdf

def attempt():
	graph = {}

	for d in data:
		d = d.split(': ')
		s = d[0]
		d = d[1].split(' ')
		if s not in graph:
			graph[s] = {}
		for x in d:
			graph[s][x] = 1
			if x not in graph:
				graph[x] = {}
			graph[x][s] = 1

	while len(graph) > 2:
		n1 = random.choice(list(graph.keys()))
		nn1 = graph[n1]
		n2 = random.choice(list(nn1.keys()))
		nn2 = graph[n2]
		nn = n1+n2
		del graph[n1]
		del graph[n2]
		del nn1[n2]
		del nn2[n1]
		for nnn in nn2:
			if nnn not in nn1:
				nn1[nnn] = 0
			nn1[nnn] += nn2[nnn]
		graph[nn] = nn1
		for nnn in nn1:
			nnnn = graph[nnn]
			cnt = 0
			if n1 in nnnn:
				cnt += nnnn[n1]
				del nnnn[n1]
			if n2 in nnnn:
				cnt += nnnn[n2]
				del nnnn[n2]
			nnnn[nn] = cnt
	return graph

while True:
	g = attempt()
	[n1,n2] = list(g.keys())
	if g[n1][n2] == 3:
		res = len(n1)*len(n2) // 9
		break

print(f"Part 1: {res}")
