#ученики и предметы

num_of_student = int(input("Write number of stident: "))
list_with_dict = []
for num in range(1, num_of_student + 1):
    name = input(f"Name of {num} student: ")
    # subjects = input(f"Subjects of {num} student: ").replace(" ", "")
    subjects = input(f"Subjects of {num} student: ").split()
    list_with_dict.append({"name":name, "subjects": subjects})
    # list_with_dict.append({"name":name, "subjects": list(map(str, subjects))})
    num += 1

# print(list_with_dict)

def show_all(d_list):
    sort_list = sorted(d_list, key=lambda i: i["name"], reverse=True)
    for i in sort_list:
        print(f"{i['name']}: {i['subjects']}")

show_all(list_with_dict)

def student_for_sub(list, name):
    # j = 0
    for i in list:
        if name == i["name"]:
            print(i["subjects"])
            # j += 1
    # if j == 0:
    #     print("There are no student with this name.")

# student_for_sub(list_with_dict, "Kate")

def sub_for_student(list, sub):
    # j = 0
    for i in list:
        if sub in i["subjects"]:
            print(i["name"])
            # j += 1
    # if j == 0:
    #     print("There is no student studying this subject")

# sub_for_student(list_with_dict, "")