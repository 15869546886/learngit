#-*- coding:utf-8 -*-
'''
数组中重复的数字
找出数组中重复的数字，在一个长度为n的数组nums里的所有数字都在0-n-1的范围内。数组中
某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复多少次。请找出数组中
任意一个重复的数字

解题思路：
哈希表法，遍历数组，将第一次找到的元素放入哈希表中，然后第二次遍历到了，如果是相同元素
就直接返回这个元素。
'''

class Solution:
    def findRepeatNumber(self,num):
        hahdict = {}
        for i,element in enumerate(num):
            if hahdict.get(element):
                return element
            else:
                hahdict[element] = 1

