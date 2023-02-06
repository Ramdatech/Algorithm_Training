import sys

def merge_sort(ls):
	if len(ls) == 1 :
		return ls
	mid = int((1+len(ls))/2)
	ls_l = merge_sort(ls[:mid])
	ls_r = merge_sort(ls[mid:])
	
	return merge(ls_l, ls_r)
	
def merge(ls1, ls2) :
	ls_l, ls_r = ls1, ls2
	i,j,tg = 0,0, []
	
	def ap(lst, idx):
		tg.append(lst[idx])
		res.append(lst[idx])
		return idx+1
	
	while i < len(ls_l) and j < len(ls_r) :
		if ls_l[i] < ls_r[j] :
			i = ap(ls_l, i)
		else :
			j = ap(ls_r, j)
	while i < len(ls_l) :
		i = ap(ls_l, i)
	while j < len(ls_r) :
		j = ap(ls_r, j)
	return tg

t = sys.stdin.readline
a, b = map(int, t().split())
ls = list(map(int, t().split()))

res = []
merge_sort(ls)

if len(res) >= b:
	print(res[b-1])
else :
	print(-1)