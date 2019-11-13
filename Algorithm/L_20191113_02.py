#-*- coding:utf-8 -*-
'''
给出第一个词first和第二个词second，考虑在某些文本text中可能以“first second third”形式出现的情况，
其中second紧随first出现，third紧随second 出现。
对每种这样的情况，将第三个词“third”添加到答案中，并返回答案
'''

class Solution(object):
	def findOcurrences(self,text,first,second):
		"""
		:type text: str
		:type first: str
		:type second: str
		:rtype: List[str]
		"""
		res = []
		a = text.split(' ')
		length_text = len(a)
		for i in range(0,length_text-2):
			if first == a[i] and second == a[i+1]:
				res.append(a[i+2])

		return res


if __name__ == '__main__':
	a = Solution()
	print a.findOcurrences("jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa","kcyxdfnoa","jkypmsxd")





				
