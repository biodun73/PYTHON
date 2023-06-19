class parent:
    def __init__(self,firstname, lastname):
        self.firstname =  firstname
        self.lastname = lastname
    def __str__(self):
        return "Your name is"+ " " + self.firstname + " " + self.lastname

p = parent("John", "Paul")
print(p)
