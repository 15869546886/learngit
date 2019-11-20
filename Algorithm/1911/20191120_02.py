#-*- coding:utf-8 -*-
'''
给定两个字符串s和t，判断他们是否是同构的。
如果s中的字符可以被替换得到t，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序，
两个字符不能映射到同一个字符上，但字符可以映射自己本身。
'''
class Solution(object):
	def isIsomorphic(self, s, t):
		hashdic = {}
		for i, c in enumerate(s):
			if hashdic.get(c):
				if t[i] != hashdic[c]:
					return False
			else:
				if t[i] in hashdic.values():
					return False
				hashdic[c] = t[i]
		return True

if __name__ == '__main__':
	a = Solution()
	print a.isIsomorphic('paper','title')

