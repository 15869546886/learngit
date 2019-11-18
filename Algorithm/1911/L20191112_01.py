#-*- coding:utf-8 -*-

'''
给定一个整数数组arr，请你帮忙统计数组中每个数的出现次数
如果每个数的出现次数都是独一无二的，就返回true；否则返回false
'''

class Solution(object):
	def uniqueOccurrences(self,arr):
		"""
		type arr: List[int]
		rtype ：bool
		"""
		counter = {}
		for n in arr:
			counter[n] = counter.get(n,0)+1
		counts = list(counter.values())
		return len(counts) == len(set(counts))

if __name__ == '__main__':
	a =Solution()
	print a.uniqueOccurrences([1,2,2,1,1,3])
