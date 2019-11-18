#-*- coding:utf-8 -*-
'''
给定一个非空的整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次，找出那个
只出现了一次的元素
说明
你的算法应该具有线性时间复杂度，你可以不使用额外空间来实现吗？
'''

class Solution(object):
	def singleNumber(self, nums):
		"""
		type nums :List[int]
		rtype :int
		"""
		hash_table = {}
		for i in nums:
			try:
				hash_table.pop(i)
			except:
				hash_table[i] = 1
		return hash_table.popitem()[0]

if __name__ == '__main__':
	a = Solution()
	print a.singleNumber([4,1,2,1,2])
