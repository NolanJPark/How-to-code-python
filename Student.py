class Student: #The name of the class must be the same as the name of the file
    def __init__(self, name, major, gpa, on_probation): #def __innit__(parameters) is the Python equivalent of a constructor
        self.name = name #self.variable
        self.major = major
        self.gpa = gpa
        self.on_probation = on_probation
    def check(self): #puttin self in is important
        if not self.on_probation and self.gpa >= 3:
            self.gpa += .5
        elif not self.on_probation:
            self.gpa += 1
        elif self.on_probation and self.gpa > 0.5:
            self.gpa -= .5
        print(self.name + " has gpa",self.gpa)
    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False