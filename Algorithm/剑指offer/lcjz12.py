#-*- coding:utf-8 -*-
'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从
矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵
的某一格，那么该路径不能再次进入该格子。例如，在下面的3X4的矩阵中包含一条字符串'bfce'的
路径,用大写字母标识出了
[['a','B','c','e'],
['s','F','C','s',],
['a','d','E','e']]
但矩阵中不包含字符串'abfb'的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子
后，路径不能再次进入这个格子。
'''

class Solution:
    def exist(self, board, word):
        

