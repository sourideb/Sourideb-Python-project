#python project
#STUDENT MODULE
def createStudent():
    ID=input("Enter student id: ")
    Name=input("Enter student Name: ")
    Roll=input("Enter Class Roll no.: ")
    BatchID=input("Enter batch id: ")
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv",'a',newline='')
    writerobj=csv.writer(fh)
    writerobj.writerow([ID,Name,Roll,BatchID])
    fh.close()
    print('Student creation successful')
    return

def updateStudent():
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv",'r',newline='')
    readerobj=csv.reader(fh)
    L=[]
    for i in readerobj:
        L.append(i)
    if len(L)==1:
        print("No record found to update")
        return

    ID=input("Enter the student id to update: ")
    print("Ready to update")
    Name=input("Enter new student name: ")
    Roll=input("Enter new Class Roll no.: ")
    BatchID=input("Enter new batch id: ")
    temp=open(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",'w',newline='')
    writerobj=csv.writer(temp)
    fh.seek(0,0)
    for i in readerobj:                    
        if i[0]!=ID:
            writerobj.writerow(i)
        else:
            writerobj.writerow([ID,Name,Roll,BatchID])

    fh.close()
    temp.close()

    os.remove(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv")
    os.rename(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",\
              r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv")
    return
    
    
def removeStudent():
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv",'r',newline='')
    readerobj=csv.reader(fh)
    L=[]
    for i in readerobj:
        L.append(i)
    if len(L)==1:
        print("No record found to remove")
        return

    ID=input("Enter student id to remove: ")
    print("Ready to remove")
    temp=open(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",'w',newline='')
    writerobj=csv.writer(temp)
    fh.seek(0,0)
    for i in readerobj:                    
        if i[0]!=ID:
            writerobj.writerow(i)


    fh.close()
    temp.close()

    os.remove(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv")
    os.rename(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",\
              r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv")
    return


def generateReportCard():
    StudentID=input("Enter the student id to generate his/her report card: ")
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv",'r',newline='')
    temp=open(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",'w',newline='')
    readerobj=csv.reader(fh)
    writerobj=csv.writer(temp)
    d={}
    writerobj.writerow(['Course Name','Marks','Grade'])
    for i in readerobj:
        nL=i[2].split(',')
        for j in nL:
            T=j.partition(':')
            if T[0]==StudentID:
                d[i[1]]=T[2]                 #d={'Python Programming':'95' , 'Physics':'65' }


    Sum=0
    for key in d:
        val=int(d[key])
        Sum=Sum+val
    avg=Sum/len(d)

    for key in d:
        if d[key]>='90':
            grade='A'
        elif d[key]>='80':
            grade='B'
        elif d[key]>='70':
            grade='C'
        elif d[key]>='60':
            grade='D'
        elif d[key]>='50':
            grade='E'
        else:
            grade='F'
        writerobj.writerow([key,d[key],grade])

    writerobj.writerow(['The total percentage is',str(avg)+'%'])
    fh.close()
    temp.close()
    os.rename(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",\
              "C:\\Users\\sonu_\\Documents\\file manipulation programs\\Report card of "+StudentID+".csv")
    return

#COURSE MODULE
def createCourse():
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv",'a',newline='')
    writerobj=csv.writer(fh)
    CourseID=input("Enter course id: ")
    CourseName=input("Enter course name: ")
    n=int(input("How many student records u want to enter?: "))
    s=''
    for i in range(n):                                 #this block makes the marks obtained string
        ID=input("Enter student id"+str(i+1)+": ")     #ex. "CSE2201:95,CSE2101:73"
        Marks=input("Enter marks obtained: ")
        if s=='':
            s=s+ID+':'+Marks
        else:
            s=s+','+ID+':'+Marks
        
    writerobj.writerow([CourseID,CourseName,s])
    fh.close()
    print("Course creation successful")
    return


def coursePerformance():                              #to show class roll no.,student name,marks obtained
    CourseID=input("Enter course id to see performance: ")
    print("Class Roll Number, Name ,Marks")
    fh1=open(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv",'r',newline='')
    fh2=open(r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv",'r',newline='')
    robj1=csv.reader(fh1)
    robj2=csv.reader(fh2)
    for i in robj1:
        break
    for i in robj2:
        break

    d={}
    for i in robj2:
        if i[0]==CourseID:          #nL=['CSE2201:95','CSE2101:73']
            s=i[2]

    nL=s.split(',')
    for i in nL:
        T=i.partition(':')
        d[T[0]]=T[2]                 #d={'CSE2201':'95' , 'CSE2101':'73'}

    for i in robj1:
        for key in d:
            if i[0]==key:
                print(i[1],i[2],d[key],sep=',')

    fh1.close()
    fh2.close()
    return
    
#BATCH MODULE
def createBatch():
    BatchID=input("Enter batch id: ")
    BatchName=input("Enter batch name: ")
    DeptName=input("Enter department name: ")
    n=int(input("Enter no. of courses : "))
    cs=''
    for i in range(n):
        CourseName=input("Enter course name: ")
        if cs=='':
            cs=cs+CourseName
        else:
            cs=cs+','+CourseName
    n=int(input("Enter no. of students: "))
    ss=''
    for i in range(n):
        StudentID=input("Enter student id: ")
        if ss=='':
            ss=ss+StudentID
        else:
            ss=ss+','+StudentID
            
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Batch.csv",'a',newline='')
    writerobj=csv.writer(fh)
    writerobj.writerow([BatchID,BatchName,DeptName,cs,ss])
    fh.close()
    return

def viewList1():
    BatchName=input("Enter batch name: ")
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Batch.csv",'r',newline='')
    readerobj=csv.reader(fh)
    print("List of Students")
    for i in readerobj:
        if i[1]==BatchName:
            L=i[4].split(',')
            print(L)
    fh.close()
    return

def viewList2():
    BatchName=input("Enter batch name: ")
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Batch.csv",'r',newline='')
    readerobj=csv.reader(fh)
    print("List of all courses")
    for i in readerobj:
        if i[1]==BatchName:
            L=i[3].split(',')
            print(L)
    fh.close()
    return

def batchPerformance():              #to show roll,name,%
    BatchName=input('Enter Batch name to see batch performance: ')
    print("Name,Roll,percentage")
    fh1=open(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv",'r',newline='')
    fh2=open(r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv",'r',newline='')
    fh3=open(r"C:\Users\sonu_\Documents\file manipulation programs\Batch.csv",'r',newline='')
    robj1=csv.reader(fh1)
    robj2=csv.reader(fh2)
    robj3=csv.reader(fh3)
    
    for i in robj1:
        break
    for i in robj2:
        break
    for i in robj3:
        break

    for i in robj3:
        if i[1]==BatchName:
            s=i[4]
    StudentList=s.split(',')       #StudentList=['CSE2201','CSE2101']
    for i in robj1:
        mL=[]
        if i[0] in StudentList:
            fh2.seek(0,0)
            for j in robj2:
                nL=j[2].split(',')
                for k in nL:
                    T=k.partition(':')
                    if T[0]==i[0]:
                        mL.append(int(T[2]))
            avg=sum(mL)/len(mL)
            print(i[1],i[2],str(avg)+'%',sep=',')

    fh1.close()
    fh2.close()
    fh3.close()
    return

#DEPARTMENT MODULE
def createDepartment():
    DeptID=input('Enter department id(Shortform): ')
    DeptName=input("Enter department name: ")
    n=int(input("Enter no. of batches: "))
    bs=''
    for i in range(n):
        BatchID=input("Enter batch id: ")
        if bs=='':
            bs=bs+BatchID
        else:
            bs=bs+','+BatchID
   
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Department.csv",'a',newline='')
    writerobj=csv.writer(fh)
    writerobj.writerow([DeptID,DeptName,bs])
    fh.close()
    return


def viewAllBatches():
    DeptID=input('Enter department id(name shortform): ')
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Department.csv",'r',newline='')
    readerobj=csv.reader(fh)
    print("List of all batches for a particular department")
    for i in readerobj:
        if i[0]==DeptID:
            L=i[2].split(',')
            print(L)
    fh.close()
    return

#EXAMINATION MODULE
def enterMarks():
    StudentID=input('Enter student id to enter marks: ')
    fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv",'r',newline='')
    temp=open(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",'w',newline='')
    readerobj=csv.reader(fh)
    writerobj=csv.writer(temp)
    d={}
    L=[]
    writerobj.writerow(['Course ID','Course Name','Marks Obtained'])
    for i in readerobj:                 #to pass the header string
        break
    for i in readerobj:
        L.append(i)

    while True:
        CourseID=input("Enter course id to enter marks of the student: ")
        Marks=input("Enter marks of the student in that course: ")
        flag=0
        for i in range(len(L)):
            if L[i][0]==CourseID:
                s=L[i][2]
        nL=s.split(',')
        for i in nL:
            T=i.partition(':')
            d[T[0]]=T[2]                #d={'CSE2201':'95','CSE2101':'73'}
        for key in d:
            if key==StudentID:
                d[key]=Marks
                flag=1
        if flag==0:
            d[StudentID]=Marks

        ms=''
        for key in d:
            s=key+':'+d[key]
            if ms=='':
                ms=s
            else:
                ms=ms+','+s
        for i in range(len(L)):
            if L[i][0]==CourseID:
                L[i][2]=ms

        ans=input("Do you want to enter marks of any other course?(y/n)")
        if ans=='n':
            break

    writerobj.writerows(L)
    fh.close()
    temp.close()
    os.remove(r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv")
    os.rename(r"C:\Users\sonu_\Documents\file manipulation programs\temp.csv",\
              r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv")
    return



#main
import csv,os
# Student file
fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Student.csv",'a+',newline='')
fh.seek(0,0)
L=[]
hl=['Student ID','Name','Class Roll Number','Batch ID']
readerobj=csv.reader(fh)
writerobj=csv.writer(fh)
for i in readerobj:
    L.append(i)
if L==[]:
    writerobj.writerow(hl)
fh.close()

#Course file
fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Course.csv",'a+',newline='')
fh.seek(0,0)
readerobj=csv.reader(fh)
writerobj=csv.writer(fh)
L=[]
hl=['Course ID','Course Name','Marks Obtained']
for i in readerobj:
    L.append(i)
if L==[]:
    writerobj.writerow(hl)
fh.close()

#Batch file
fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Batch.csv",'a+',newline='')
fh.seek(0,0)
readerobj=csv.reader(fh)
writerobj=csv.writer(fh)
L=[]
hl=['Batch ID','Batch Name','Department Name','List of courses','List of students']
for i in readerobj:
    L.append(i)
if L==[]:
    writerobj.writerow(hl)
fh.close()

#Department file
fh=open(r"C:\Users\sonu_\Documents\file manipulation programs\Department.csv",'a+',newline='')
fh.seek(0,0)
readerobj=csv.reader(fh)
writerobj=csv.writer(fh)
L=[]
hl=['Department ID','Department Name','List of batches']
for i in readerobj:
    L.append(i)
if L==[]:
    writerobj.writerow(hl)
fh.close()

while True:
    print()
    print("Choose the module")
    print("1.Student")
    print("2.Course")
    print("3.Batch")
    print("4.Department")
    print("5.Examination")
    print("6.Exit")
    print()
    option=input('Enter option number: ')
    print()

    if option=='1':
        print("Choose what to do in Student Module")
        print("1.Create a Student")
        print("2.Update the Student Details")
        print("3.Remove a Student from Database")
        print("4.Generate report card of a Student")
        chk=input('Enter option number: ')
        if chk=='1':
            createStudent()
        elif chk=='2':
            updateStudent()
        elif chk=='3':
            removeStudent()
        elif chk=='4':
            generateReportCard()
        else:
            print("Wrong option chosen!")
            
    elif option=='2':
        print("Choose what to do in Course Module")
        print("1.Create a new course")
        print("2.View performance of all students in the course")
        chk=input('Enter option number: ')
        if chk=='1':
            createCourse()
        elif chk=='2':
            coursePerformance()
        else:
            print("Wrong option chosen")
            
    elif option=='3':
        print("Choose what to do in Batch Module")
        print("1.Create a new batch")
        print("2.View list of all students in a batch")
        print("3.View list of all courses taught in the batch")
        print("4.View complete performance of all students in a batch")
        chk=input('Enter option number: ')
        if chk=='1':
            createBatch()
        elif chk=='2':
            viewList1()
        elif chk=='3':
            viewList2()
        elif chk=='4':                                   
            batchPerformance()
        else:
            print('Wrong option chosen')

    elif option=='4':
        print("Choose what to do in Department Module")
        print("1.Create a new department")
        print("2.View all batches in a department")
        chk=input('Enter option number: ')
        if chk=='1':
            createDepartment()
        elif chk=='2':
            viewAllBatches()
        else:
            print("Wrong option chosen")
        
    elif option=='5':
        print("Choose what to do in Examination Module")
        print("1.Enter marks of all students for a specific examination")
        print("2.View performance of all students in the examination")
        chk=input('Enter option number: ')
        if chk=='1':
            enterMarks() 
        elif chk=='2':
            coursePerformance()
        else:
            print("Wrong option chosen")

    elif option=='6':
        print("Thank you :)")
        break
    else:
        print("Wrong option chosen")
