#These are all the code for the visa coding competition

#The password should have a minimum length of 8 characters.
#It should have atleast one english alphabet which can either be lowercase or uppercase or both.
#It should have atleast one numeric character.
#It should have atleast one special character among these: [@, $, %, &, *].

#libaries needed
#Run the python script, there are test cases on the bottom

import re

#function that returns True or False if the password is valid
def is_valid(s):

    #TODO: Check to see if length is less than 8.
    min_len = 8
    if(len(s) < min_len):
        print("Password {} does not meet the length requirement".format(s))
        return False


    #TODO: Check to see there is a alpha character in password
    substr = re.search('[a-zA-z]', s)       #look for alpha characters, gives none if no alpha
    if(substr == None):
        print("Password {} does not have an alphabet letter".format(s))
        return False

    #TODO: Check to see if there is a numeric character
    substr = re.sub('[0-9]', '', s)      #take away all numbers
    value = s is substr                     #if s is still the same than it has no numbers characters
    if(value == True):
        print("Password {} does not have a numeric letter".format(s))
        return False

    #TODO: Check to see if there  is at least one of [@, $, %, &, *]
    substr = re.search('[@\$\%\&\*]', s)
    if(substr == None):
        print("Password {} does not have a special character".format(s))
        return False

    return True

#Test case 1: Not valid email with len(s) < 8
s = "not_8"
valid = is_valid(s)

output = ""
output = "VALID" if(valid) else "INVALID"
print(output)

#Test Case 2: Not valid email-Passes length requirement, not alpha case
s = "249823498"
valid = is_valid(s)

output = ""
output = "VALID" if(valid) else "INVALID"
print(output)

#Test Case 3: Not valid email-Pases first two cases, not number case
s = "MPasswordTest"
valid = is_valid(s)

output = ""
output = "VALID" if(valid) else "INVALID"
print(output)

#Test Case 4: Not valid email-Passes first 3 cases, not special character case
s = "Nocharacter18"
valid = is_valid(s)

output = ""
output = "VALID" if(valid) else "INVALID"
print(output)

#Test Case 5: Valid email: Passes all cases
s = "Mariano18@@"
valid = is_valid(s)

output = ""
output = "VALID" if(valid) else "INVALID"
print(output)
