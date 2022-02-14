class Tomato:
    states = {"недозревший": 1, 'середина созревания': 2, "созревший": 3}

    def __init__(self, index, state=states["недозревший"]):
        self._index = index
        self._state = state

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for i in self.tomatoes:
            Tomato.grow(i)

    def all_are_ripe(self):
        x = []
        for i in self.tomatoes:
            z = Tomato.is_ripe(i)
            x.append(z)
        if all(x) == True:
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()

    def pp(self):
        print(self.tomatoes)


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Садовник начал работать!")
        TomatoBush.grow_all(self._plant)
        print("Садовник закончил работать!")
        print("---------------------------")

    def harvest(self):
        if TomatoBush.all_are_ripe(self._plant) == True:
            print("Садовник собрал урожай.")
            print("---------------------------")
            TomatoBush.give_away_all(self._plant)
        else:
            print("Еще не все помидоры созрели!")
            print("---------------------------")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству")
        print("---------------------------")


Gardener.knowledge_base()
g = TomatoBush(10)
gg = Gardener("Дима", g)
gg.work()
gg.harvest()
gg.work()
gg.harvest()
