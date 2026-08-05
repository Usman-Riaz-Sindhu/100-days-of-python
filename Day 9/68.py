# a dictionary is a key value paried list that stores data in a key value format. It is a collection of unordered, changeable, and indexed data types. In Python, dictionaries are written with curly brackets, and they have keys and values.
# {key : value}
dictionary = {"name": "Usman Riaz Sindhu", "age": 21, "city": "Pattoki", "Profession": "Computer Science Student", "university": "University of Veterinary and Animal Science", "country": "Pakistan"}
# print(dictionary["name"])  # Output: Usman Riaz Sinhu
# print(dictionary["Profession"])  # Output: Computer Science Student

# if we do not provide a key as same as in the dictionary then it will give us an error. For example, if we try to access a key that does not exist in the dictionary, it will raise a [KeyError].

# Also providing same data type as key will not give us an error but it will overwrite the previous value of that key. For example, if we have a dictionary with a key "name" and we try to add another key "name" with a different value, it will overwrite the previous value.

# **********Adding new key value pair in dictionary**********
dictionary["hobby"] = "Playing Cricket"
# print(dictionary)  # Output: {'name': 'Usman Riaz Sindhu', 'age': 21, 'city': 'Pattoki', 'Profession': 'Computer Science Student', 'university': 'University of Veterinary and Animal Science', 'country': 'Pakistan', 'hobby': 'Playing Cricket'}

# dictionary = {}
# print(dictionary)  # Output: {} 
# dictionary["name"] = "Ahmad Riaz Sindhu"
# print(dictionary)  # Output: {'name': 'Ahmad Riaz Sindhu'}

for d in dictionary:
    print(d)  # Output: name
    print(dictionary[d])  # Output: Ahmad Riaz Sindhu