class House:

    has_kitchen = True

    def __init__(self, name, limit_floor):
        self.name = name
        self.limit_floor = limit_floor

    def __del__(self):
        print(f'{self.name} is exit')

    def __len__(self):
        return self.limit_floor

    def __str__(self):
        return f'name is: {self.name}, number of foolrs: {self.limit_floor}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.limit_floor == other.limit_floor
        else: return 'типы объектов не совпадают'

    def __lt__(self, other):
        return self.limit_floor < other.limit_floor
    def __le__(self, other):
        return self.limit_floor <= other.limit_floor
    def __gt__(self, other):
        return self.limit_floor > other.limit_floor
    def __ge__(self, other):
        return self.limit_floor >= other.limit_floor
    def __ne__(self, other):
        return self.limit_floor != other.limit_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.limit_floor = self.limit_floor + 10
            return self
        else: return 'типы объектов не совпадают'

    def __iadd__(self, value):
        if isinstance(value, int):
            self.limit_floor += value
            return self
        else: return 'типы объектов не совпадают'

    def __radd__(self, value):
        if isinstance(value, int):
            self.limit_floor = value + self.limit_floor
            return self
        else: return 'типы объектов не совпадают'




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print('-'*20)
print(h1 == h2)
print('-'*20)

h1.__add__(h2) # увеличиваем количество этажей)
h1.__iadd__(10)
h2.__radd__(10)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
print()

print(House.has_kitchen)
print()
