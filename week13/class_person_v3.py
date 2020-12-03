class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def say(self):
        print(f'{self.name} say')

    def eat(self):
        print(f'{self.name} eat')


andy = Person('Andy', 'male')
andy.say()
andy.eat()

