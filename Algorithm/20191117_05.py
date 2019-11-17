#-*- coding:utf-8 -*-
'''
给定仅有小写字母组成的字符串数组A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）
组成的列表。例如，如果一个字符在每个字符串中出现3次，而不是4次，则需要在最终答案中包含
该字符3次
你可以按任意顺序返回答案
'''
class Solution(object):
	def commonChars(self, A):
		ans = []
		s = set(A[0])
		for i in s:
			num = min(a.count(i) for a in A)
			ans.extend(i*num)
		return ans

if __name__ == '__main__':
	a = Solution()
	print a.commonChars(["bella","label","roller"])

