#-*- coding:utf-8 -*-
'''
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块最重的石头，然后将他们一起粉碎。假设石头的重量分别为x，y
且x<=y，那么，粉碎的可能结果如下：
如果x == y ，那么两块石头都会被完全粉碎；
如果x != y,那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x
最后，最多只会剩下一块石头，返回此石头的重量，如果没有石头剩下，返回0
'''
class Solution(object):
	def lastStoneWeight(self, stones):
		"""
		:type stones: List[int]
		:rtype: int
		"""
		while len(stones)>1:
			stones.sort()
			if stones[-1] == stones[-2]:
				stones.pop(-1)
				stones.pop(-1)
			else:
				stones[-1] = stones[-1] - stones[-2]
				stones.pop(-2)
		if len(stones) != 0:
			return stones[0]
		return 0

if __name__ == '__main__':
	a = Solution()
	print a.lastStoneWeight([2,7,4,1,8,1])
