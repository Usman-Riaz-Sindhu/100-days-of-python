# we can also use a list or another dictionary as a value in a dictionary. For example, we can have a dictionary with a key "hobbies" and the value can be a list of hobbies.
list = ["Playing Cricket", "Reading Books", "Watching Movies"]
dictionary = {"name": "Usman Riaz Sindhu", "age": 21, "city": "Pattoki", "Profession": "Computer Science Student", "university": "University of Veterinary and Animal Science", "country": "Pakistan", "hobbies": list}
# print(dictionary)  # Output: {'name': 'Usman Riaz Sindhu', 'age': 21, 'city': 'Pattoki', 'Profession': 'Computer Science Student', 'university': 'University of Veterinary and Animal Science', 'country': 'Pakistan', 'hobbies': ['Playing Cricket', 'Reading Books', 'Watching Movies']}
# 
hobbies_dictionary = {"hobbies": ["Playing Cricket", "Reading Books", "Watching Movies"]}
dictionary["hobbies"] = hobbies_dictionary["hobbies"]
print(dictionary)  # Output: {'name': 'Usman Riaz Sindhu', '
# 


capitals = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome"}
travel_log = {"France": ["Paris", "Lyon", "Marseille"], "Germany": ["Berlin", "Munich", "Frankfurt"], "Italy": ["Rome", "Milan", "Venice"]}

print(travel_log["France"][1])  # Output: Lyon
print(travel_log["Italy"][2])

nested_list = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(nested_list[1])  # Output: f
# rhis is called nested list because it is a list inside a list. We can access the elements of the nested list by using the index of the outer list and then the index of the inner list. For example, to access the element "e" in the nested list, we can use nested_list[1][1]. The first index 1 refers to the second list in the outer list, and the second index 1 refers to the second element in that inner list.

nested_dictionary = {"dict1": {"key1": "value1", "key2": "value2"}, "dict2": {"key3": "value3", "key4": "value4"}}
print(nested_dictionary["dict1"]["key2"])  # Output: value2

dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dict["key2"])  # Output: value2