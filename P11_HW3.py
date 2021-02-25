##3. В класі Name визначте:
##атрибути для first name та last name (fname та lname відповідно);
##атрибут fullname що повертає first і last names;
##атрибут initials який повертає ініціали (перші літери first та last name,
##розділених ‘.’ .

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + " " + lname
        self.initials = fname[0].upper() + "." + lname[0].upper() + "."
