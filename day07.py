#!/usr/bin/python3

def get_input():
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r


year = 2023
day = 7

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

res = 0

card_ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':(1 if part2 else 11), 'Q':12, 'K':13, 'A':14}

hand_ranks = {"11111":1, "2111":2, "221" :3, "311":4, "32":5, "41":6, "5":7}

hands = []

for d in data:
	[h,m] = d.split(' ')
	x = {}
	for c in card_ranks:
		x[c] = 0
	for c in h:
		x[c] = x[c] + 1
	numj = x['J'] if part2 else 0
	x = [c1 for c,c1 in x.items() if c1 > 0 and (not part2 or c != 'J')]
	x.sort()
	x.reverse()
	if x == []:
		x = [5]
	else:
		x[0] = x[0] + numj
	l = "".join([str(y) for y in x])
	ll = [hand_ranks[l]]
	for c in h:
		ll.append(card_ranks[c])
	hands.append((tuple(ll),int(m)))

hands.sort()
for i in range(len(hands)):
	res = res + (i+1)*hands[i][1]

print(f"Part {2 if part2 else 1}: {res}")

