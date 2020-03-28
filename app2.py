# What is "import" sys doing?
import sys

# This function takes input and validates that all of the required input is there
def getArgs():
    if len(sys.argv) == 3:    
        # what is the bracket '[1]' doing?
        age = str(sys.argv[1])
        name = str(sys.argv[2])
    else:
        print ('This program requires input.  Example app.py <age> <name>.  python app.py 40 Tom')
    return(age, name)

# Add an appropriate comment here
def thePrintFunction( character_age, character_name):
    print("there was a man named " + character_name + ", " )
    print("he was " + character_age + "," )
    print("he liked his name " + character_name + "," )
    print("but didn't like that he was " + character_age + ",")

# Added bonus, create another function (not required)

# what is this if statment doing?  
if __name__ == '__main__':
   age, name = getArgs()
   thePrintFunction(str(age), str(name))