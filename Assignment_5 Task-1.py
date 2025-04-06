dict={'Alice':85,'Johnny':90}
n=input("Enter the student's name: ")
if n in dict:
    print(n+"'s","marks:",dict.get(n))
else:
    print("Student not found")