#GLOBAL VARIABLES

# FUNCTIONS ARE BLOCK OF CODES THAT WORKS ONLY WHEN CALLED 
user = 'peter'
def say_hello(name):
    global user
    user = 'Paul'
    print('hello welcome ' +user)
    
    
say_hello(user)