#-*- coding:utf-8 -*-
'''
适配器模式：解决接口不兼容的问题
结构型设计模式通过组合对象来实现新功能，适配器模式通过引入间接层来实现
不兼容接口之间的适配。现实中最好的例子就是手机充电口，不同型号安卓手机
都可以用同样的充电线充电。在python中可以通过继承实现适配，也可以通过
使用class的__dict__属性。开闭原则：适配器模式和OOP中的开闭原则关系
密切，开闭原则强调对扩展开放，对修改关闭。通过适配器模式我们可以通过创建
适配器模式在不修改原有类代码的情况下实现新的功能。
'''

class Computer:
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        """ call by client code """
        return 'execute a program'

class Synthesizer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electroinc song'

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} human'.format(self.name)

    def speak(self):
        return 'say hello'

class Adapter:
    def __init__(self, obj, adapted_methods):
        """不使用继承，使用__dict__属性实现适配器模式"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

#适配器使用示例
def main():
    objs = [Computer('Asus')]
    synth = Synthesizer('moog')
    objs.append(Adapter(synth,dict(execute=synth.play)))
    human = Human('Wnn')
    objs.append(Adapter(human,dict(execute=human.speak)))

    for o in objs:
        #用统一的execute适配不同对象的方法，这样在无需修改源对象的情况下就实现了不同对象方法的适配
        print('{} {}'.format(str(o),o.execute()))

if __name__ == '__main__':
    main()