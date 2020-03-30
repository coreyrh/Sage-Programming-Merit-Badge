# What is "import" sys doing? the import part is saying to import the sys. sys is what lets the interpreter understand
# variables and other code a person would write
import sys


# This function takes input and validates that all of the required input is there
def getArgs():
    try:
        age = str(sys.argv[1])
        name = str(sys.argv[2])
    except:
        print('This program requires input.')
        print('Syntax: python app.py <age> <name>')
        print('Example: python app2.py 40 Tom')
        print('')
        print('Using example as defaults')
        print('')
        return "40", "Tom"

    else:
        return age, name


# Add an appropriate comment here
def thePrintFunction(character_age, character_name):
    print("there was a man named " + character_name + ", ")
    print("he was " + character_age + ",")
    print("he liked his name " + character_name + ",")
    print("but didn't like that he was " + character_age + ",")


# Added bonus, create another function (not required)

# what is this if statement doing? This takes the info a person writes and assigns it to the variable base off the
#order written in
if __name__ == '__main__':
    age, name = getArgs()
    thePrintFunction(str(age), str(name))
