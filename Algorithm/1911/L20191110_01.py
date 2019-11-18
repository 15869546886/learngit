#-*- coding:utf-8 -*-
'''
给定一个数组，它的第i个元素是一支给定股票第i天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）
注意：你不能同时参与多比交易（你必须在再次购买前出售掉之前的股票）
'''

class Solution(object):
	def maxProject(self,prices):
		"""
		:type prices:List[int]
		:rtype:int
		"""
		price = 0
		for i in xrange(1,len(prices)):
			tem =prices[i] -prices[i-1]
			if tem >0:
				price +=tem
		return price

if __name__ == '__main__':
	a = Solution()
	print a.maxProject([7,1,5,3,6,4])
