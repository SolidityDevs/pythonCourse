class User:
    
    def __init__(self, name,age,favourite_subject):
        self.name = name
        self.age = age
        self.subject = favourite_subject
        
    def B(self):
        return f'Name: {self.name}\nAge: {self.age}\nSubject: {self.subject}'
        
    

print(User(name='David',age=5,favourite_subject='Python').B())


#print(caller.name)


#INHERITANCE
#ILTERATORS
#SCOPE
#MODULES
    