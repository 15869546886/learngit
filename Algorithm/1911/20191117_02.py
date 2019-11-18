#-*- coding:utf-8 -*- 
'''
在显示着数字的坏的计算器上，我们可以执行以下两种操作：
双倍：将屏幕上的数字乘2；
递减：将显示屏上的数字减1.
最初，计算机显示数字X
返回显示数字Y所需的最小操作数
'''
class Solution(object):
	def brokenCalc(self, X, Y):
		"""
		type X : int 
		type Y : int
		rtype :int
		"""
		res = 0
		while Y > X:
			res += 1
			if Y%2:
				Y += 1
			else:
				Y /= 2
		return res + X - Y
if __name__ == '__main__':
	a=Solution()
	print a.brokenCalc(2,3)
			
