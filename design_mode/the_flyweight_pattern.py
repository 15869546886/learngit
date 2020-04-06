#-*- coding:utf-8 -*-
'''
享元模式：实现对象复用从而改善资源使用
OOP编程中容易出现对象创建带来的性能和内存占用问题，需要满足以下条件：
--需要使用大量对象（python里我们可以用__slots__节省内存占用）
--对象太多难以存储或解析大量对象
--对象识别不是特别重要，共享对象中对象比较会失败
疆场使用对象池技术来实现共享对象，比如数据经常使用连接池来减少开销，预先建立
一些连接池，每次取一个连接和数据库交互。
'''
import random
from enum import Enum
TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree:
    pool = dict()
    
    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if obj is None:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj
    
    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type,age,x,y))

def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                rnd.randint(min_point, max_point),
                rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                rnd.randint(min_point, max_point),
                rnd.randint(min_point, max_point))
        tree_counter += 1
    
    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                rnd.randint(min_point, max_point),
                rnd.randint(min_point, max_point))
        tree_counter += 1
    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))
    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))

if __name__ == '__main__':
    main()