##1. В класі Person визначте метод compare_age(), який повертатиме результат
##порівняння віку людини з Вашим віком. При заданих об’єктах p1, p2 і p3, які
##будуть ініціалізовані name та age, буде повертатися повідомлення наступного
##формату:
##{other_person} is {older than / younger than / the same age as} me.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self):
        difference = self.age - 22
        if difference > 0:
            return self.name + " is older than me."
        if difference < 0:
            return self.name + " is younger than me."
        if difference == 0:
            return self.name + " is the same age as me."
