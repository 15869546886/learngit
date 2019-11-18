#-*- coding:utf-8 -*-
'''
给你一份词汇表（字符串数组）words和一张字母表chars
假如你可以用chars 中的字母（字符）拼写出words中的某个单词（字符串），那么我们就认为
你掌握了这个单词
注意:每次拼写时，chars中的每个字母都只能用一次。
返回词汇表words中你掌握的所有单词的长度之和。
'''
class Solution(object):
	def countCharacters(self, words, chars):
		dic = {}
		for i in chars:
			if dic.get(i):
				dic[i] += 1
			else:
				dic[i] = 1
		res = 0
		for word in words:
			a = 0
			for j in word:
				if dic.get(j) and word.count(j) <= dic[j]:
					a += 1
				else:
			 		break
			if a ==len(word):
				res += a
		return res

if __name__ == '__main__':
	a = Solution()
	print a.countCharacters(["cat","bt","hat","tree"],"atach")


