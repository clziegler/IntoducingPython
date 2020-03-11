# 10.1
class Thing:
    pass


print(Thing)

example = Thing

print(example)


# 10.2
class Thing2:
    letters = 'abc'


print(Thing2.letters)


# 10.3
class Thing3:
    letters = ''


letters = Thing3
letters.letters = 'xyz'

print(letters.letters)


# 10.4, 10.6, 10.8
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'

    @property
    def get_name(self):
        return self.name

    @property
    def get_symbol(self):
        return self.symbol

    @property
    def get_number(self):
        return self.number


atom = Element('Hydrogen', "H", 1)

# 10.5
atom_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**atom_dict)

atom.dump()
hydrogen.dump()

# 10.7
print(hydrogen)
# 10.8
print(hydrogen.get_name)
print(hydrogen.get_number)
print(hydrogen.get_symbol)

# 10.9
class Animal:
    def __init__(self, food):
        self.food = food

    def eats(self):
        return self.food

class Bear(Animal):
    pass

class Rabbit(Animal):
    pass

class Octothorp(Animal):
    pass

yogi = Bear('berries')
bugs = Rabbit('clover')
gumby = Octothorp('campers')

print(yogi.eats())
print(bugs.eats())
print(gumby.eats())


# 10.10
class Laser:
    def does(self):
        return "Disintegrate"


class Claw:
    def does(self):
        return "Crush"


class Smartphone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        return f'{self.laser.does()} {self.claw.does()} {self.smartphone.does()}'


dalek = Robot()

print(dalek.does())

