#-*- coding:utf-8 -*-
'''
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回true，如果数组中每个元素都
不相同，则返回false。
'''

class Solution(object):
	def containDuplicate(self, nums):
		hashdic = {}
		for i in range(len(nums)):
			if nums[i] not in hashdic:
				hashdic[nums[i]] = 1
			else:
				return True
		return False



if __name__ == '__main__':
	a = Solution()
	print a.containDuplicate([1,2,3,1])
