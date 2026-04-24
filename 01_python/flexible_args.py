def student_info(*args, **kwargs):
    info = {}
    
    for key, value in kwargs.items():
        info[key.capitalize()] = value
    
    if args:
        info["Extra"] = list(args)    
    return info

stu1 = student_info(Name="Mohsin", roll=664900)
print("Student 1 : ", stu1)

stu2 = student_info("Math", 121, Name="Mohsin", roll=664900)
print("Student 2:", stu2)