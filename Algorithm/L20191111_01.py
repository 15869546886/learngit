#-*- coding:utf-8 -*-
'''
在一个平衡字符串中，“L” 和 “R”的数量是相同的
给出一个平衡字符串s，请你将它分割成尽可能多的平衡字符串
返回可以通过分割得到的平衡字符串的最大数量
'''

class Solution(object):
	def balancedStringSplit(self, s):
		"""
		:type s:str
		:rtype:int
		"""
		judge = 0
		res = 0
		length = len(s)
		for i in s:
			if i == 'L':
				judge += 1
			elif i == 'R':
				judge -=1
			if judge == 0:
				res +=1
		return res


if __name__ == '__main__':
	a = Solution()
	print a.balancedStringSplit('RLRRLLRLRL')
