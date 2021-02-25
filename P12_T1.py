# Suppose we want to ensure that the car model should always be between 2000 and
# 2018. If a user tries to enter a value less than 2000 for the car model, the
# value is automatically set to 2000 and if the entered value is greater than
# 2018, it should be set to 2018. If the value is between 2000 and 2018, it
# should not be changed. 

class Model:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2018:
            self.__year = 2018
        else:
            self.__year = year

    def display(self):
        return "The car model is " + str(self.year)
