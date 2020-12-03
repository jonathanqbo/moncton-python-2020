class Person:

    def __init__(self, name, gender='male'):
        self.name = name
        self.gender = gender

    def say(self, words):
        print(f'{self.name} say {words}')

    def eat(self, foods):
        print(f'{self.name} eat {foods}')


zijun = Person('Zijun')
zijun.say('I am superman')
zijun.eat('lobster')

