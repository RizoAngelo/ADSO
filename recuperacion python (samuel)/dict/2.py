student_id = {1711: "Erick", 1152: "Kyles", 115: "papa"}

print("inicio  Dictionary: ", student_id)

del student_id[1711]

print("final Dictionary ", student_id)
for i,a in student_id.items():
    print(a)

key, value="pepe","juan"
student_id[key]=value
print(student_id)