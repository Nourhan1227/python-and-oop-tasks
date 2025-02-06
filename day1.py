#ask user about these info.
full_name = input("Enter your full name: ")
age = int(input("Enter your age: ")) + 1
faculty = input("Enter your faculty: ")
birth_date = input("Enter your birth date (YY/MM/DD) :  ")
graduation_year = input("Enter your graduation year: ")


#print the info
print(f"the Full_name is : {full_name} \n The age is: {age} \n The Faculty is {faculty} \n  Birthdate is:  {birth_date}\n The Graduation year is: {graduation_year}")




diskspace=int(input("pls enter the disk space percentage"))
if diskspace < 10:
    print("Warning: Low disk space!")
elif 10 <= diskspace <= 20:
    print("Warning: Disk space is getting low.")
else:
    print("Disk space is sufficient.")