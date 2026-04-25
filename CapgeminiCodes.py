#DAY 1
#list
'''l=[1,2,3,4,5]
l.append(6)
print(l)
l.extend([7,8])
print(l)
l.pop(1)
print(l)
l.remove(1)
print(l)
l.clear()
print(l)
#print(dir(list))
a=[1,2,[3,4]]
a[2][0]=30
print(a)
#tuple
t=(1,1,1,1,2,4,54)
print(type(t))
print(dir(tuple))
print(t.count(1))
print(t.index(2))
#set
s={1,2,3,4,5,6,7}
print(type(s))
print(dir(set))
s.add(8)
print(s)
p=s.copy()
print(p)
s.remove(3)
print(s)
s.discard(1)
print(s)'''
#DAY2
'''print(math.sqrt(576))
print(type(a))
print(float())
bc=5j
print(bc1)
print(type(bc))
print(complex())
bd=True
print(type(bd))
print(bool())
print(True+True)
u='cgc'
print(type(u))
print(id(u))
print(u[1])'''
#DAY 3
'''a='Dilpreet'
print(a[1])
print(a[-3])
print(a.upper())
print(a.lower())
print(a.isupper())
print(a.islower())
print(a.title())
b="Hello World"
print(b.capitalize())
c='1234567'
print(c.isdigit())
st="sasassssadasd"
print(st.count('s'))
str="The class is going on"
print(str.split())
xc="the class- is going-on"
print(xc.split('-'))# split on the basis of '-'
bv="     The class is of python   "
print(bv.strip())
print(dir(str))#The function with ___ are calles magic method or split method
sd="12dsds"
print(sd.isalnum())'''
#DAY 4
#LIST
'''a=[1,2,3]# homogenous data type
b=[1,2,3]# heterogenous data type
print(type(a))
print(list())# false,[],0
a.append(4),a.append(5)# it only takes one argument
print(a)
a.extend([6,7])# it takes two or more arguments
print(a)
a.pop()#remove last value by default
a.pop(1)# remove value at dedicated index
print(a)
a.remove(5)# remove dedicated value in list
print(a)
a.clear() # clear all the values from the list
print(a)
print(dir(list))
print(dir(int))
a[2]=40
print(a)
# 0 1 2
v=[1,2,[3,4]]
# 0 1 indexes
# print(v)
n=v[2][0] #3 access the value at 2nd index of v and 0 of 2nd
print(n)
v[2][0]=20  converts 3 into 20
print(v)
# TUPLE
a=(1,2,3,2,2,2,,54,54)
print(type(a))
print(tuple())
# print(dir(tuple)) # display all methods
# print(len(dir(tuple)))
print(a.count(2))
print(a.index(3)) return the index of dedicated value
print(a.index(2)) if value repeats then it only return index of first value given,1
# SET
#cannot add mutable data type in set but add immutable data type
a={1,2,3,4}
print(a)
print(type(a))
#print(dir(set))
a.add(30)#{1,2,3,30}
a.add("adsd")
print(a)
b=a.copy()
print(b)
a.remove("adsd")# give error if given value is  not present in set
print(a)
a.discard(50)# dont give error if the value is not in the set
print(a)'''
#DAY5
#DICT
'''a= input("enter:")
an={"Dilpreet":18}
print(an)# print full dictionary {'Dilpreet':18}
print(an[a])#print the key value a is key in dict "an" 18
ax={"list":[1,2,3],23:"Dilpreet","dp":2007}
print(ax[23])
ax["new"]=20#insert new key or value in dict
ax["new"]=300 # update new value not create new key value
print(ax)
#we can add only immutable data type in as key
# int,float,complex,bool,str,tuple can be used as  keys
# METHODS
d=ax.copy()
print(d)
ax.pop(23)
print(ax)
ab={"Dilpreet":18,"dsa":21}
ab.popitem()# remove the last element by default
print(ab)'''
#DAY6
'''ls=[1,2,300,[20,30]]
ls2=ls
ls[2]=30 # if we make change in one list then due to same address it will also reflect in list 2 in general copy method
print(ls2)
ls3=[1,30,[234,556]]
ls4=ls3.copy() # shallow copy, inner layer --> reference address is copied, outer layer--> directly copied
print(ls4)
ls3[3][1]=322
print(ls3)#[1,2,35,[234,322]] changed outer layer in ls3 only
print(ls4)#[1,2,30,[234,322]] element changed in both lists inner layer in shallow copy because only inner address are same of ls3 andls4
import copy
ls5=[32,34,54,[43,56]]
ls6=copy.deepcopy(ls5)
print(ls6)
ls5[1]=45
ls5[3][0]=40
print(ls5) #[32,45,54,[40,56]] only change reflect in ls5
print(ls6) #[32,34,54,[43,56]] change not reflects  in ls6 in deepcopy only values copied initially'''
 # DAY7
 # OPERATORS
 # Arithmetic operators :*,-,*,/,%,**,//
 # Comparison operators:==,!=,>,<,<=,>=
 # logical operators: and, or,not
 #Bitwise operators :Performs operators on bit by bit value
 # coverting decimal to binary value:

'''print(bin(34))
# octal to binary
print(oct(11))
#hexadecimal to binary
print(hex(11))
#Bitwise AND &
print(2&3)#2 first convert decimal values to binary than compare then according to logical (and)
#Bitwise OR !
print(2(3))#3
#Bitwise NOT ~
print(~2) #-3 Formula ~(oprand+1)
#Bitwise XOR ^
print(2^3) #1 return 0 on same input or 1 on different input
#Bitwise Left shift <<
print(5<<2)#20
#As 5= 101 in binary 
# in Left shift   1  0  1
#               1<-0<-1<-0 (1)
#            1<-0<-1<-0<-0 (2)
# final        10100


#Bitwise Right Shift >>
print (5>>2) #1
#As  5=101 binary
#       1   0  1 | fall
#      -->1-->0 |-> 1  fall (1)
#       -->  |->0  fall (2)
# Finall 1 binary 
# Membership oprators: in ,not in
#Identity operators : is , is not works on (-5 to 256)
a=260
b=260
print(a is b)# in this we are comparing their addresses acc. to range(-5 t o 256) same addresses
 #Input/ Output functions
# eval identify datatype by itself of given value
a=eval(input())
print(a,type(a))# "Dilpreet" <class 'str'>
 
 #output
print (2,3,4,sep='@',end='@') #2@3@4#'''
 #DAY 8
#CONTROL STATEMENTS
#IF
'''a=int(input("enter age"))
if(a>=18):
    print("eligible")
else:
    print("not eligible")
    #Q1. WAP to print square of a no. if it is divisible by 9 if not print cube.
v=float(input("enter a number"))
if v%9==0:
    print(v**2)
else:
    print(v**3)
# Q2 WAP to check if  student has secured A grade , B grade, C grade ,D grade. 90,80,70,50.
marks=int(input("enter the marks of the student"))    
if(marks>=90):
    print("A grade")
elif(marks>=80):
    print("B grade")
elif(marks>=70):
    print("C grade")
elif(marks>=50):
    print("D grade")
else:
    print("FAIL")

#Q3 WAP to  get output as reminder if htrer no. divisible by 2 if not check if it is aa multiple of 5 if not print I AM OK.
num= int(input("enter a num"))
if num%2==0:
    print("reminder is zero")
elif num%5==0:
    print(f,"{num}" is a multiple of 5)# appstring method
else:
    print("I AM OK")'''
          
 # NESTED IF 
 # Q4     WAP to check if the no is a two digit num or not if a two digit is even print its square else print remainder. else print it is not rwo digit no.
'''no=int(input("Enter the no"))
if  no>=10 and no<=99:
    print("it is a two digit no")
    if no%2==0:
        print("it is even")
        print("square", no**2)
    else:
        print("remainder",no%2)
        print("it is not two digit no")'''
#DAY 9
#Looping statement: while or for
# while Syntax
#initialization
#while condition:
#statement block
#updation of condition
#Reverse while loop
'''n=10
while n>=1:
    print(n)
    n-=1
    #print square of even or cube of odd range 50.
n=1
while n<=50:
    if n%2==0:
        print("even square",n,",",n**2)
    else:
        print("odd cube",n,",",n**3)
        n+=1
    #count no. of digit in a number.
n=int(input("enter number"))
cnt=0
while n!=0:
    n%10!=0
    cnt=cnt+1
    n=n//10
    print(cnt)
    #DAY 10
    #SLICING IN STRING
    #SYNTAX[ start indx:end indx+-1:undating step]
car="range rover" #11
print(car[6:12:1])
#slicing in list
ls=[1,2,3,4,5,6,7]
print(ls[0:7:2]) #[1,3,5,7]   
print(ls[::-1]) #[7,6,5,4,3,2,1]
#range function 
print(range(11)) # range(0,11) dont print 0 to 11
print(list(range[11])) #[0,1,2,3,4,5,6,7,8,9,10]
print(tuple(range[11])) # (0,1,2,3,4,5,6,7,8,9,10)
print(str(range[7]))    # range (0,7)
# Range with list
print(list(range(1,11))) #[1,2,3,4,5,6,7,8,9,10]
print(list(range(1,11,2))) #[1,3,5,7,9]
# Range wth tuple
print(tuple(range(-1,-11,-2))) #(-1,-3,-5,-7,-9)
#Access elements of list using for loop
lis=[11,12,13,14,15]
for i in lis:
    print(i,end="") # 11 12 13 14 15
# in tuple 
tup=(101,200,132)
for i in tup:
    print(i,end="") # 101 200 132
# in set
s1={1,2,3}
for i in s1:
    print(1,end="")'''#1 2 3
    # NOTE : while dont work with  set or dict.
   #DAY 11
'''ls=[10,78,15,41,56]
target=41
for i in ls:
    if i==target:
        print("Number found at ","index",ls.index(i))
        break'''
#WAP To find the largest value in list
'''ls=[10,78,15,41,56]
max_val=float('-inf')
sec_large=float("-inf")
for i in ls:
    if i> max_val:
        sec_large=max_val
        max_val=i
    elif i> sec_large and i!= max_val:
         print(max_val)
    for i in ls:
            sec_large=0
            if i>sec_large:
                sec_large=i
                print(sec_large)'''
#DAY 12 Functions
'''a=10
b=20
print(a+b)
print("hello")
c=12
d=23
print(c+d)
 #FUNCTION = it is a block of code used to perform some specific task . you can call n no of times. it will work only after the calling.
 syntax= def fun__name(argument):
 example addition ()
def addition(): # fnc declaration and fnc definition and calling.
a= int (input("ENTER A"))          |
b= int(input("ENTER B"))           |   function body
print("addition of a and b ",a+b)  |
addition()
print("hello")
addition()
def addition():
there are two types of function.
1= inbuilt function
2= user defined function
inbuilt fnc= utility= those fnc which can be useb with mostly all of the datatypes eg= id(),type(),len(),print()
def add(a,b):
    print(a+b)
    add(2,3)
formal arguments= these are the variables name that are given while function calling
types=
actual arguments=
Types of user defined fnc on the basis of return type and argument'''
# DAY 13
'''
Nested for loop
for i in range(3):       #& & & 
                         #& & & 
                         #& & &
    for j in range(3):
        print("&",end=' ')
    print()

ls=[1,2,3,4,4,5,4,6,4]
a=0
for i in ls:
    a+=1
    for j in range(a,len(ls)-2):
      
        if i==ls[j]:
            ls.remove(i)
print(ls) #[1, 2, 3, 5, 6, 4]

#Functions
#return, not argu
def uppercase():
    st=input("Enter string:")
    st=st.upper()
    return st

print(uppercase())

#return , argu
def addition(a,b):
    a=a+10
    b=b+10
    c=a+b
    return c
print(addition(20,30))
#FORMAL ARGUMENTS:
 def name(arguments)
1. positional arg:-
2. keyword arg:-
3. Default arg:-'''
#DAY 14 # FUNCTIONS
'''4.variable length/ var length arg:-
def sum(*a):
    sum(1,2,3,4,5,6,7)
def sum(a,b,*c):
    sum(1,2,3,4,5,6,7)
# WAP to design the sum of the numbers
def sum(*a):# Arguments are with  * called args stores values as tuple takes only positional arguments.
    sum=0
    for i in a:
        sum= sum+i
    print(sum)
sum(1,2,3,4,5) # 15 
# ARGUMENTS  def sum(*a)                                                               # KWARGS def sum(**a)
it is represented in the form of single asterik.                 it is represented in the form of double asterick.
it only takes positional arguments.                              it only take keyword arg.
it stores values as a collection in tuple.                       it stores values as an collection in dict.

# var length work on packing or unpacking
data=2,3,4 # TUPLE
print(data[0])
l=eval(input())
def 

#GLOBAL AND LOCAL VARIABLE:-
a=10 # GLOBAL :[ these are the variable which are declared outside the fnc and can be used anywhere inside the program]
def dilpreet():
    b=11 # LOCAL :[these are the variables which are declared inside the fnc and can only be access inside the fnc]
    print(a)
    print(b)
dilpreet()
print(a)
print(b)# CANT Exist
# take a list
L=[1,2,3,4]
def dilpreet():
    L=[4,5,8,9]
    print(L)
    print(id(L))
dilpreet()
print(L)
print(id(L))
# 
L=[1,2,3,4]
def dilpreet():
    global L # global keyword is used to print the same value.
    L=[4,5,8,9]
    print(L)
    print(id(L))
dilpreet()
print(L)
print(id(L))
#WAP To print this output using var length argument using fnc. Name-'dilpreet'
#                                                              Age- 18
#                                                              course-'AIDS'
def unkown(**d):
    for key,value in d.items():
        print(key,'-',value)
        unkown(Name='dilpreet',Age=27,Course='AIDS')
#DAY 15 BITWISE OPR.
a=5
b=3
a&b
a|b
a^b
~a
~b
a<<2
a>>1
# merge and sort without built in fnc.
l1=[3,1,2,4]
l2=[3,1,2,3]
# WAP to output = "nohtyp si yrev doog" without slicing and in build fnc
s="Python is very good"'''
# DAY 16 CLASS AND OBJECT
'''class classname: # CLASS SYNTAX                            
object=classname() # OBJECT CREATION 
class- it is a blue print or template. it is having the property. it stores data or properties, functionalities and behaviour.
class is a container which hold prop. and functionalities of real time entities.
class have property and funtion.function
ex:- Laptop:- function= black, length,weight.
property= start ,stop,ram.'''
'''class Car:
    brand=None
    colour=None
    hp=None
    # OBJECT CREATION
obj1= Car()
obj2=Car()
obj3=Car()
print(obj1.brand)
print(obj2.brand)
print(obj3.brand)
Car.colour='red'
print(Car.colour)
print(obj1.colour)
obj1.colour='blue'
obj2.colour='green'
obj3.colour='red'
print(obj1.colour)
print(obj2.colour)
print(obj3.colour)'''
# WAP TO create a class for hospital and assign some properties.
class hospital:
    name=' HOSPITAL '
    patient=69
    floor=20
    nurse=50
    doctor=10
obj1=hospital()
obj2=hospital()
obj3=hospital()
obj4=hospital()
obj5=hospital()
print(obj1.name)
print("patient",obj2.patient)
print("floor",obj3.floor)
print("nurse",obj4.nurse)
print("doctor",obj5.doctor)
class college:
# STATIC/Class properties.
    clg_name='CGC'
    timing='all day'
    loc='Chandigarh'
st1= college()
#specific properties / object properties.
st1.name ='Dilpreet'
st1.rollno='6969'
st1.section= 'B'
print(st1.clg_name,st1.timing,st1.loc,st1.name,st1.rollno,st1.section)

# static and specific properties



#FUNCTION in class becomes method.
#WAY 1

class bank():
    bankname="SBI"
    IFSC="SBI000123"
    country="india"
    def details(obj,name,age,phone,pan,bal):
        obj.name="Dilpreet"
        obj.age="18"
        obj.phone="7837620950"
        obj.pan=""
        obj.bal=""
        #WAY2
c1=bank()
c1.details('Dilpreet',18)
c2=bank()
c2.details('Dilpreet',18)
#WAY3
#__init__=
#cls,self=
class bank():
    bankname="SBI"
    branch="HYD"
    IFSC="SBI000123"
    def __init__(self):
        c1=bank('dilpreet',18)
'''TYPES OF METHOD
 1= object/instance=
 2=class=
 3=static=
 4=abstract=
 #EXAMPLE
class bank():
    #static property
    bname="sbi"
    branch="HYD"
    #constructor(to auto initialize value to the particular obj.)
    def __init__(self,name,age,balance):
        self.name=name
        self.age=age
        self.bal=balance
        #object method
    def display(self):
        print(self.name,self.age,self.bal)
    def change_age(self,new_age):
        self.age=new_age

        #class method
        @classmethod
        def change_bdetails(cls,new_branch):
            cls.branch=new_branch
            #class method
            @classmethod
            def bank_details(cls):
                print(cls.bname,cls.branch)

# inheritance:-
1 single
2 multiple
3 multilevel
4 hybrid
5 hierarchial'''











 

 







    
























  
















