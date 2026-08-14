# if we wanna make a global variable that we never want to change we can use the uppercase naming convention to indicate that it is a constant variable and should not be changed. However, this is just a convention and does not enforce immutability in Python.

# PI = 3.14 #constant variable
# GOOGLE_URL = "https://www.google.com" #constant variable

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)