class Person:
    def __init__(self, param_name):
        print("person class", param_name)
        self.name = param_name

    def talk(self):
        print("안녕하세요 제 이름은", self.name, "입니다.")


person_1 = Person("함성호")
print(person_1)
person_1.talk()
person_2 = Person("장혜민")
print(person_2)
person_2.talk()
