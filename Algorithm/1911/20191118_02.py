#-*- coding:utf-8 -*-
'''
小A和小B在玩猜数字游戏。小B每次从1,2,3中随机选择一个，小A每次也从1,2,3中选择一个猜。
他们一共进行三次游戏，请返回小A猜对了几次？
输入的guess数组为小A每次的猜测，answer数组为小B每次的选择，guess和answer的长度都等于3
'''
class Solution(object):
	def game(self,guess,answer):
		return sum(guess[i] == answer[i] for i in range(len(guess)))

if __name__ == '__main__':
	a = Solution()
	print a.game([1,2,3],[1,2,3])
