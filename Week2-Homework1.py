students = ["Sarp Yılmaz", "Etem Coşkun"]
print(students)

print("******************")

def studentAdd():
    name = input("eklenecek öğrenci adını girin:")
    surname = input("eklenecek öğrencinin soyadını girin:")
    students.append(name+" "+surname)
    print("öğrenci listeye eklendi.")
    print(students)

studentAdd()

print("**************")

def studentRemove():
    name = input("silinecek öğrenci adını girin:")
    surname = input("silinecek öğrenci soyadını girin:")
    students.remove(name+" "+surname)
    print("öğrenci listeden kaldırıldı.")
    print(students)
studentRemove()

print("**************")

def studentsAdd():
    number = int(input("Kaç tane yeni öğrenci eklenecek:"))
    for i in range(number):
        addstudent = input("yeni eklenecek öğrencinin adı ve soyadı:")
        students.append(addstudent)
        i +=1
        print("öğrenciler listeye eklendi.")
        print(students)

studentsAdd()

print("**************")

def studentList():
    student = 0
    for student in range(len(students)):
        print(students[student])
        student += 1
print("öğrenciler listelendi")
studentList()

print("*****************")

def studentNumberFind():
   student = input("Numarası öğreneilecek öğrencinin adı soyadı: ")
   i=0
   while i < len(students):
    if students[i] == student:
        print("Öğrenci numarası: ")
        print(i)
        break
    i +=1
studentNumberFind()

print("****************")
