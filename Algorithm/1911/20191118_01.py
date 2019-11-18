#-*- coding:utf-8 -*-
'''
给定由N个小写字母字符串组成的数组A，其中每个字符串长度相等。
删除 操作的定义是：选出一组要删掉的列，删去A中对应列中的所有字符，形式上，第n列
为[A[0][n],A[1][n],...,A[A.length-1[n]].
'''
class Solution(object):
	def minDeletionSize(self, A):
		ans = 0
		for col in zip(*A):
			if any(col[i] > col[i+1] for i in xrange(len(col) - 1)):
				ans +=1
		return ans


if __name__ == '__main__':
	a = Solution()
	print a.minDeletionSize(["cba","daf","ghi"])
