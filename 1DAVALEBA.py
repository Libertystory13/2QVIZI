class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

    def __eq__(self, other):
        return self.name == other.name


apple1 = Fruit('apple', 2)
banana = Fruit('banana', 3)
apple2 = Fruit('apple', 5)
lemon = Fruit('lemon', 3)

print(apple1 + banana)
print(apple1 == apple2)
print(apple2 == lemon)