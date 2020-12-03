class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.__stomach = 'stomach'

    def say(self):
        print(f'{self.name} say')

    def eat(self):
        print(f'{self.name} eat')
        self.__digest()

    def __digest(self):
        print(f'{self.__stomach} is digesting food')


andy = Person('Andy', 'male')
andy.eat()
# andy.__digest()  # private method/attribute is not available for invoke from outside
