#-*- coding:utf-8 -*-
'''
给定字符串s和t，判断s是否是t的子序列
示例：
s=“abc”，t="ahbgdc"
'''

class Solution(object):
	def isSubsequence(self,s,t):
		"""
		:type s:str
		:type t:str
		:rtype:bool
		"""
		point_s = 0
		point_t = 0
		length_s = len(s)
		length_t = len(t)
		while point_s<length_s and point_t<length_t:
			if s[point_s] == t[point_t]:
		   		point_s +=1
	 		point_t+=1

		return point_s ==length_s

if __name__ == '__main__':
	a = Solution()
	print a.isSubsequence('abc','ahbgdc')
   				
