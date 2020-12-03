class Person:

    def __init__(self, name, gender='male'):
        self.name = name
        self.gender = gender

    def say(self, words):
        print(f'{self.name} say {words}')

    def eat(self, foods):
        print(f'{self.name} eat {foods}')


class PythonCampStudent(Person):

    school = 'Moncton Python Camp'
    teacher = 'MR Q'

    def __init__(self, name, gender='male'):
        super().__init__(name, gender)

    def study(self):
        print(f'{self.name} learn python with {self.teacher} at {PythonCampStudent.school}')

    def do_homework(self):
        print(f'{self.name} do python homework from teacher {PythonCampStudent.teacher} at {self.school}')


zixie = PythonCampStudent('Zixie')
zixie.say('I am a billionaire')
zixie.eat('apple')
zixie.study()
zixie.do_homework()

