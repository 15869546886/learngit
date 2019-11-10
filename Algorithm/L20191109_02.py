#-*- coding:utf-8 -*-
'''
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值得那两个整数
并返回他们的数组下标
'''


class Solution(object):
	def twoSum(self, nums,target):
		"""
		:type nums :List[int]
		:type target : int
		:rtype :List[int]
		"""
		hashmap = {}
		for ind,num in enumerate(nums):
			hashmap[num] = ind
		for i,num in enumerate(nums):
			j = hashmap.get(target - num)
			if j is not None and i!=j:
				return [i,j]


if __name__ == '__main__':
	a = Solution()
	print a.twoSum([2,7,11,15],9)
