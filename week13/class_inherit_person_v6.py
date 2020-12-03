class Person:

    def __init__(self, name, gender='male'):
        self.name = name
        self.gender = gender

    def say(self, words):
        print(f'{self.name} say {words}')

    def eat(self, foods):
        print(f'{self.name} eat {foods}')


class Student(Person):

    def __init__(self, name, school, gender='male'):
        super().__init__(name, gender)
        self.school = school

    def study(self, knowledge):
        print(f'{self.name} learn {knowledge}')

    def do_homework(self):
        print(f'{self.name} do homework')


zixie = Student('Zixie', 'Evergreen Park School', 5)
zixie.say('I am a billionaire')
zixie.eat('apple')
zixie.study('python')
zixie.do_homework()
print(zixie.school)

