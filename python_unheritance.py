class parent:
    def __init__(self,firstname, lastname):
        self.firstname =  firstname
        self.lastname = lastname
    def __str__(self):
        return "Your name is"+ " " + self.firstname + " " + self.lastname
class child(parent):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
p = child("John", "Paul")
print(p)
