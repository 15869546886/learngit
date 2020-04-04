#-*- coding:utf-8 -*-

class Frog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """不同类型玩家遇到的障碍不同"""
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))

class Bug:
    def __str__(self):
        return 'a bug'
    
    def action(self):
        return 'eats it'

class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n-----Frog World-----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()

class Wizard:
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the wizard battles against {} and {}!'.format(
            self, obstacle, obstacle.action())) 

class Ork:
    def __str__(self):
        return 'an evil ork' 
    
    def action(self):
        return 'kill it'

class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t ------ Wizard World -----'
    
    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

class GameEnvironment:
    """抽象工厂，根据不同的玩家类型创建不同的角色和障碍（游戏环境）
    这里可以根据年龄不同，成年人返回巫师游戏，小孩返回青蛙过河游戏"""
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)