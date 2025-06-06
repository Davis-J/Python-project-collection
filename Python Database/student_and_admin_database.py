Name=[]
Id=[]
Grade=[]
TotalMarks=[]
def Project():
  print("Enter 1 to enter as admin \nEnter 2 to enter as student \nEnter 3 to exit")
  x=int(input(": "))
  if x==1 or x==2:
    Password()
  elif x==3:
    exit(0)
  else:
    print("Please enter a valid choice from 1 to 3")
    Project()
def Password():
  AdminPassword='Admin183'
  StudentPassword='Password798'
  y=input("Enter Password: ")
  if y==AdminPassword:
    AdminEntry()
  elif y==StudentPassword:
    StudentEntry()
  else:
    print("Password does not match with the student or admin. Please try again")
    Password()
def AdminEntry():
  print("1. Add new students \n2. Remove Students \n3. Show all data \n4. Exit")
  z=int(input(": "))
  if z==1:
    R=int(input("Enter the amount of students you want to add: "))
    for g in range(R):
      a=input("Enter name of student: ").upper()
      b=input("Enter the Id of student: ").upper()
      c=input("Enter Grade of the student: ").upper()
      d=int(input("Enter the total marks of the student: "))
      if g!=R-1:
        print("Enter the details of the next student:-")
      Name.append(a)
      Id.append(b)
      Grade.append(c)
      TotalMarks.append(d)
    AdminEntry()
  elif z==2:
    idrange=int(input("Enter the amount of students you want to remove: "))
    for G in range(idrange):
      I=input("Enter the Id of student to be removed: ").upper()
      if I in Id:
        Index=Id.index(I)
        Name.pop(Index)
        Id.pop(Index)
        Grade.pop(Index)
        TotalMarks.pop(Index)
        AdminEntry()
      else:
        print("Invalid Id")
        idrange+=1
  elif z==3:
    for q in range(len(Name)):
      print(Name[q],"has Id number", Id[q],"and is studying in",Grade[q],"with total marks as",TotalMarks[q])
    AdminEntry()
  elif z==4:
    exit(0)
    Project()
  else:
    print("Enter a valid choice")
    AdminEntry()
def StudentEntry():
  print("1. Show my student details \n2. Show my total marks \n3. Exit")
  X=int(input(": "))
  if X==1:
    IdNum=input("Enter your ID Number: ").upper()
    if IdNum in Id:
      Index2=Id.index(IdNum)
      print("Name is",Name[Index2])
      print("Id Number is",Id[Index2])
      print("Grade is",Grade[Index2])
      StudentEntry()
    else:
      print("Enter Valid Id")
      StudentEntry()
  elif X==2:
    IdNum=input("Enter your ID Number: ").upper()
    if IdNum in Id:
      Index3=Id.index(IdNum)
      print("The total marks for the student",Name[Index3],"is",TotalMarks[Index3])
      StudentEntry()
    else:
      print("Enter Valid Id")
      StudentEntry()
  elif X==3:
    exit(0)
    Project()
  else:
    print("Enter valid choice")
    StudentEntry()
Project()
#Passwords:-
#Admin- 'Admin183'
#Student-'Password798'