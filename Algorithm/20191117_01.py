#-*- coding:utf-8 -*-
'''
给定一个整数数组A，我们只能用以下方法修改该数组：
我们选择某个索引i并将A[i]替换为-A[i]替换为-A[i],然后总共重复这个过程K次（我们可以多次选择同一个索引i）
以这种方式修改数组后，返回数组可能地最大和。
'''

class Solution(object):
	def largestSumAfterKNegations(self, A, K):
		"""
		:type A: List[int]
		:type K: int
		:rtype: int
		"""
		A.sort()
		if A[K-1] <= 0:
			for i in range(K):
				A[i] = -A[i]
			return sum(A)
		for i in range(K):
			if A[i] < 0:
				A[i] = -A[i]
			else:
				break
		if not (K-i) % 2:
			return sum(A)
		A.sort()
	 	A[0] = -A[0]
   		return sum(A)

if __name__ == '__main__':
	a = Solution()
	print a.largestSumAfterKNegations([4,2,3],1)
