# Module 6 Practice 3

class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


# Для прибавления dx к x_distance по примеру из 5 модуля 3 практики
# магические методы __add__ __iadd__ __radd__


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        super(Horse, self).__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


# цепочка наследования:
# Pegasus > Horse > Eagle > object

# print(Pegasus.mro())

# Пример работы программы:

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
