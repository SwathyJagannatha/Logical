class Base:
    # Constructor to set Data
    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role

# Intermediate Class: Inherits the Base Class
class Intermediate(Base):
    # Constructor to set age
    def __init__(self, age, name, roll, role):
        super().__init__(name, roll, role)
        self.age = age

# Derived Class: Inherits the Intermediate Class
class Derived(Intermediate):
    # Method to Print Data
    def __init__(self, age, name, roll, role):
        super().__init__(age, name, roll, role)

    def Print_Data(self):
        print(f&quot;The Name is : {self.name}&quot;)
        print(f&quot;The Age is : {self.age}&quot;)
        print(f&quot;The role is : {self.role}&quot;)
        print(f&quot;The Roll is : {self.roll}&quot;)

# Creating Object of Base Class
obj = Derived(21, &quot;Lokesh Singh&quot;, 25, &quot;Software Trainer&quot;)

# Printing the data with the help of derived class
obj.Print_Data()