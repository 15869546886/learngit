#-*- coding:utf-8 -*-
'''
给定两个整数A和B，返回任意字符串S，要求满足：
S的长度为A+B，且正好包含A个‘a’字母与B个‘b’字母；
子串‘aaa’没有出现在S中
子串'bbb'没有出现在S中
'''
class Solution(object):
	def strWithout3a3b(self, A, B):
		res = ""
		while A or B:
			if A > B:
				if A > 1:
					res += "aa"
					A -= 2
				else:
					res += "a"
					A -= 1
				if B > 0:
					res += "b"
					B -= 1
			elif A < B:
				if B > 1:
					res += "bb"
					B -= 2
				else:
					res += "b"
					B -= 1
				if A > 0:
					res += "a"
					A -= 1
			else:
				res += "ab"
				A -= 1
				B -= 1
		return res 
if __name__ == '__main__':
	a = Solution()
	print a.strWithout3a3b(5,1)
				
