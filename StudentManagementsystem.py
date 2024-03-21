#Initialize empty lists and dictionary
students_list = []
students_dict = {}

#add student information
name = input("Enter studnet's name: ")
age = input ("Enter student's age: ")
grade = input ("enter student's grade")
students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}
print("student information added successfully!")
print(students_dict.items())

#Search for a student by name
search_title =input ("Enter the name of the student to search or simply enter to skip: ")
