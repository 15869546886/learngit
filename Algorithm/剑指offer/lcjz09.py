#-*- coding:utf-8 -*-
'''
用两个栈实现一个队列。队列的声明如下。请实现它的两个函数 appendTail 和 deleteHead,
分别完成在队列尾部插入整数和队列头部删除整数的功能。（若队列中没有元素，deleteHead操作
返回-1）
'''
'''
解题思路：
两个栈实现一个队列，栈后进先出，队列先进先出，添加元素的时候，用append就能加入到队列内了，
然后弹出元素的时候，需要弹出队列内的第一个元素，先将栈1的元素从尾部弹出，然后压入到栈2内，
实现一个倒序，全部压入到栈2后，然后弹出栈2的尾部元素，实现删除，如果新增元素，继续压入到栈1
内，然后需要删除元素的时候，栈2还有元素，就继续弹出栈2的元素。如果没了，就从栈1再倒序到栈2
压一遍实现。
'''

class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        self.stack1.append(value)

    def deleteHead(self):
        if self.stack2:
            return self.B.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(1)
    print(obj)
    param_2 = obj.deleteHead()