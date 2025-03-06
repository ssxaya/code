import random

class User():

    happy = 100
    age = 0

    def __init__(self, str, fac , iq, hom):
        self.physique = str
        self.family = hom
        self.wisdom= iq
        self.looks = fac
        self.age = 0

    def set_physique(self, str):
        self.physique = str

    def set_family(self, hom):
        self.family = hom

    def set_wisdom(self, iq):
        self.wisdom = iq

    def set_looks(self, fac):
        self.looks = fac

    def add_physique(self, str):
        self.physique += str
    def add_family(self, hom):
        self.family += hom
    def add_wisdom(self, iq):
        self.wisdom += iq
    def add_looks(self, fac):
        self.looks += fac
    def add_happy(self, x):
        self.happy += x




class UserBehavio():


    def start(self,user):
        n = random.randint(0+user.family,20)
        if 0<= n <= 3:
            if n == 0:
                print("你是孤儿，生活在穷乡僻壤的小巷内，你是一个乞丐")
                user.add_happy(-5)
                user.add_looks(-7)
                user.add_wisdom(-3)
                user.add_physique(+1)
                user.add_family(0)
            if n ==1:
                print("你是孤儿，生活在小县城附近，依靠救济勉强度日")
                user.add_happy(-5)
                user.add_looks(-3)
                user.add_wisdom(-3)
                user.add_physique(-2)
                user.add_family(+1)
            if n ==2:
                print("你是穷人，父母是捡破烂的，家里依靠政府救济补贴勉强度日")
                user.add_happy(-3)
                user.add_looks(-1)
                user.add_wisdom(-4)
                user.add_physique(+3)
                user.add_family(+2)
            if n ==3:
                print("你是穷人，全靠家里父母维持的小生计度日")
                user.add_happy(0)
                user.add_looks(-1)
                user.add_wisdom(+1)
                user.add_physique(-3)
                user.add_family(+3)
        elif 4<= n <= 7:
            if n == 4:
                print("你出生在一个小县城的落魄家庭，父母每月出城打工，你和奶奶生活在一起")
                user.add_happy(1)
                user.add_looks(-1)
                user.add_wisdom(-4)
                user.add_physique(+3)
                user.add_family(+2)


