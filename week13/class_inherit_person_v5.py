class Person:

    def __init__(self, name, gender='male'):
        self.name = name
        self.gender = gender

    def say(self, words):
        print(f'{self.name} say {words}')

    def eat(self, foods):
        print(f'{self.name} eat {foods}')


class Child(Person):

    def help_parent(self, something):
        print(f'{self.name} help parent on {something}')

    def clean_room(self):
        print(f'{self.name} clean my room')


jiaze = Child('Jiaze')
jiaze.say('I am super smart')
jiaze.eat('burger')
jiaze.help_parent('catch animals')
jiaze.clean_room()

