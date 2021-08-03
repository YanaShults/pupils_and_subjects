#ученики и предметы

num_of_student = int(input("Write number of stident: "))
dict_with_children = {}
for num in range(1, num_of_student + 1):
    name = input(f"Name of {num} student: ")
    subjects = input(f"Subjects of {num} student: ").split()
    dict_with_children[name] = subjects

print(dict_with_children)

def show_all(dict):
    for i in sorted(dict.keys(), reverse=True):
        print(i, ':', dict[i])

# print(show_all(dict_with_children))

def student_for_sub(list, name):
    print(list.get(name, "No student with that name"))

# student_for_sub(dict_with_children, "Kate")

def sub_for_student(list, sub):
    stud = []
    for key, value in list.items():
        if sub in value:
            stud.append(key)
    if len(stud) == 0:
        print("There are no matching student.")
    else:
        print(stud)

# sub_for_student(dict_with_children, "math")