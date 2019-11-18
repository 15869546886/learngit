#-*- coding:utf-8 -*-
'''
给定两个正整数x和y，如果某一整数等于x^i+y^j,其中整数 i>=0且j>=0,那么我们认为该整数
是一个强整数
返回值小于或等于bound的所有强整数组成的列表
你可以按任何顺序返回答案，在你的回答中，每个值最多出现一次
'''
class Solution(object):
	def powerfulIntegers(self, x, y, bound):
		ans = set()
		for i in xrange(20):
			for j in xrange(20):
				v = x**i + y**j
				if v <= bound:
					ans.add(v)
		return list(ans)

if __name__ == '__main__':
	a = Solution()
	print a.powerfulIntegers(2,3,10)
