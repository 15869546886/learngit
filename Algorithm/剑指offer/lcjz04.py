#-*- coding:utf-8 -*-
'''
二维数组中的查找
在一个n*m的二维数组中，每一行都是从左到右递增的顺序排序，每一列都是从上到下
递增的顺序排序。请完成一个函数，输入这样一个二维数组和一个整数，判断数组中是
否有该整数

解题思路：
最开始想的是用暴力法两个遍历去求解，但是我没有用到这个递增的特性，应该不是最
优解，利用递增特性，从左下角或者右上角开始和这个值进行比较，比如从左下角开始，
左下角的值为martrix[i][j],如果这个值比左下角的值大的话，我将j++，然后继续
比较，找出是否有值和这个值相同，如果这个值比左下角的值小的话，我将i--，然后继
续比较，找出是否有值相同，全部比对完，没有返回False，然后最后需要考虑martrix
为空的情况，直接返回False。
'''

class Soultion:
    def findNumberIn2dArray(self, martrix, target):
        i, j = len(martrix)-1, 0
        if not martrix:
            return False
        while i >=0 and j < len(martrix[0]):
            if target < martrix[i][j]:
                i -= 1
            elif target > martrix[i][j]:
                j += 1
            else:
                return True
        else:
            return False