import random
class Voin(object):
    def __init__(self, a):
        self._unit = a
    
    def get(self):
        return self._unit
    
    def set(self, hp):
        self._unit = hp
    
    def fight(self1, self2):
        while self1.get() > 0 and self2.get() > 0:
            who_is_first = random.randint(1,2)
            if who_is_first == 1:
                self2.set(self2.get() - 20)
                print('Первый юнит ударил. Оставшееся здоровье:')
                print('Первый юнит:', self1.get())
                print('Второй юнит:', self2.get())
            if who_is_first == 2:
                self.set(self1.get() - 20)
                print('Второй юнит ударил. Оставшееся здоровье:')
                print('Первый юнит:', self1.get())
                print('Второй юнит:', self2.get())
        if self2.get() == 0:
            print('Победил первый юнит')
        else:
            print('Победил второй юнит')
unit1 = Voin(100)
unit2 = Voin(100)
unit1.fight(unit2)