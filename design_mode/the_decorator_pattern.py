#-*- coding:utf-8 -*-
'''
装饰器模式：无需子类化实现扩展对象功能问题
通常给一个对象添加新功能有三种方式：-直接给对象所属的类添加方法。-使用【组合】-使用
【继承】，优先使用组合而非继承。装饰器模式提供了第四种选择，通过动态改变对象扩展对象
功能。其他编程语言通常使用继承实现装饰器装饰器模式，而python内置了装饰器。装饰器有很多
用途，比如数据校验，事务处理，缓存，日志等。比如用装饰器实现一个简单的缓存，python3.5
自带了funtools.lru_cache
'''
from functools import wraps

def memoize(fn):
    known = dict()

    @wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer

@memoize
def fibonacci(n):
    assert(n>=0), 'n must be >=0'
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)