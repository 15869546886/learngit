#-*- coding:utf-8 -*-

'''
给你一个字符串text，你需要使用text中的字母来拼凑竟可能多的单词“ballon”
字符串text中的每个字母最多只能被使用一次，请你返回最多可以拼凑出多少个单词“balloon”
'''
import collections
class Solution(object):
	def maxNumberOfBalloons(self,text):
		"""
		type text:str
		rtype: int
		"""
		d = collections.Counter(text)
		print d
		return min(d['b'],d['a'],d['l'] // 2,d['o'] // 2,d['n'])





if __name__ == '__main__':
	a = Solution()
	print a.maxNumberOfBalloons("nlaebolko")
