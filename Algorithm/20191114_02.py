#-*- coding:utf-8 -*-
'''
公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。
'''
class Solution(object):
	def twoCitySchedCost(self,costs):
		"""
		:type costs: List[List[int]]
        :rtype: int
        """
		costs.sort(key = lambda x :x[0] - x[1])
	 	total = 0
   		n = len(costs) // 2
		for i in range(n):
			total +=costs[i][0] + costs[i+n][1]
		return total

if __name__ == '__main__':
	a = Solution()
	print a.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
