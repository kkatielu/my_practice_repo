class Student:
    def __init__(self, fname, lname, id, energy_level = 10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
        return (self.lname + ": " + self.id)
    
    def greeting(self):
        return ("Hello, I'm " + self.fname)
    
    def take_exam(self):
        self.energy_level -= 1

    def get_energy_level(self):
        return self.energy_level