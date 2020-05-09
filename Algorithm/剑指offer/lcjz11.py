#-*- coding:utf-8 -*-
'''
旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
输出旋转数组的最小元素。例如，数组[3,4,5,1,2]为[1,2,3,4,5]的一个旋转，该数组的最小值为1.

解题思路：
将列表遍历，寻找前面元素大于后面元素的情况。如果出现大于的情况，则返回后面元素。如果遍历完没有，
则返回第一个元素
看其他的解法，用了2分法求解，先将代码抄到下面
'''

class Solution:
    def minArray(self, numbers):
        for i in range(len(numbers)):
            if numbers[i-1] > numbers[i]:
                return numbers[i]
        return numbers[0]

#method2
class Solution:
    def minArray(self, numbers):
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i+j)//2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]