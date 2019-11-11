#-*- coding:utf-8 -*-

'''
数轴上放置一些筹码，每个筹码的位置存在数组chips中。
你可以对任何筹码执行下面两种操作之一（不限操作次数，0次也可以）
。将第i个筹码向左或者向右移动2个单位，代价为0.
。将第i个筹码向左或者向右移动1个单位，代价为1，
最开始的时候，同一位置上也可能放着两个或者更多的筹码。
返回将所有筹码移动到统一位置（任意位置）上所需的最小代价。
'''

class Solution(object):
	def minCostToMoveChips(self, chips):
		"""
		:type chips:List[int]
		:rtype int
		"""
		num1 = 0
		num2 = 0
		for i in chips:
			if i % 2 == 0:
				num1 += 1 
			elif i % 2 != 0:
				num2 += 1
		
		return min(num1,num2)

if __name__ == '__main__':
	a = Solution()
	print a.minCostToMoveChips([1,2,3])
