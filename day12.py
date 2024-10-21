#!/usr/bin/python3

def get_input():
	url = f"https://adventofcode.com/{year}/day/{day}/input"
	fn = f"day{day:02d}.txt"
	f = open(fn, "rt")
	r = f.read()
	f.close()
	return r

year = 2023
day = 12

input_data = get_input()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

def check(s1,s2,nums,sss):
	l = [len(x) for x in s1.split('.') if x != '']
	if len(s1) > 0 and s1[-1] == '.':
		if len(l) > len(nums) or l != nums[:len(l)]:
			return 0
		if sum(l) + s2.count('#') > sss:
			return 0
	if s2 == "":
		if l == nums:
			return 1
		return 0
	if s2[0] == '?':
		return check(s1+'#',s2[1:],nums,sss)+check(s1+'.',s2[1:],nums,sss)
	else:
		return check(s1+s2[0],s2[1:],nums,sss)

def check2(s,nl,l,p,nums,mg,visited):
	ls = len(s)
	if ls > l:
		return 0
	if mg > len(nums):
		return 0
	for i in range(ls-nl,ls):
		if p[i] != '?' and s[i] != p[i]:
			return 0
	if nums == []:
		if ls == l:
			return 1
		else:
			to_add = "."*(l-ls)
			return check2(s+to_add, len(to_add), l, p, [], 0, visited)
	if (ls,len(nums)) in visited:
		return visited[(ls,len(nums))]
	rp = 0
	while ls + rp < l and p[ls+rp] != '#':
		rp += 1
	r = 0
	for nd in range(rp+1): # l-ls-len(nums)+1
		to_add = ("."*nd)+nums[0]+("." if len(nums) > 1 else "")
		nr = check2(s+to_add,len(to_add),l,p,nums[1:],mg-1,visited)
		r += nr
	visited[(ls,len(nums))] = r
	return r


res = 0
ii = 0
for d in data:
	[s,ns] = d.split(' ')
	ns = [int(x) for x in ns.split(',')]
	if part2:
		s = [s]*5
		s = "?".join(s)
		ns = ns*5
	r = check2("",0,len(s),s,["#"*x for x in ns],len([x for x in s.split('.') if x != '' and '#' in x]),{})
	res += r
	ii += 1

print(f"Part {2 if part2 else 1}: {res}")
