#print("python")
#x:int = 10
#y:float = 6.3
# comment
#x=10
#casting
#v1= float(x)
#print (v1 ,type(v1))
#input
#x= input("Enter a number")
#print(x)
#logical operation
#math operation
#order of operation
#if statmant
'''
x= int(input("Enter a number: "))
if x > 0 :
    print(x ,"is greater")
    print("Done")
elif x < 0 :
    print(x ,"is greater")
    print("Done")
else:
    print(x ,"is not greater")
 '''

# loobs
'''
i = 0
while i < x :
    print(i)
    i = i + 1
for i in range(5):
        print(i)
        i = i + 1
 for i in renge(10):
     for j in renge(10):
         print(j)
'''
#control statmant (break)

#Exception [try: code ]
# except Exception as ex:
#the code
'''
while True:
    try:
        x = int(input("Enter a number 1 : "))
        y = int(input("Enter a number 2 : "))
        print("div = " , x/y )
        break
    except ValueError as ex:
        print("please enter a number")
'''
# list , tupel , Dictionary  [] imutable , () un imutable , {}

'''
x= [2,3,4,5,]
y= (2,3,4,5,)
z= {2: "mohamed",3: "ali",4 : 10,5:'a',}
print(x[0])
print(z[2])
print("x= ",x)
print("y= ",y)
print("z= ",z)
'''

'''x= [1,"ali" ,3.4 , 'a']
for i in range(4):
    x[i] = input("Enter a number : ")
for j in x:
    print(x[j])

print(x[1:3])'''

#Bulit in function

#file

"""x = open("abdo.txt","w")
x.write("Abdelrahman")
x.close()
"""

#function

"""def x():
    print("x")
x() #calling

def sum(a,b):
    return a+b
print(sum(1,2))

def info(name,age):
    print("name",name)
    print("age",age)

x=input("enter your name : ")
y=input("enter your age : ")
print(info(name="ali",age=18))
print(info(name="ali",age=18))

def info(**kwargs):
    print(kwargs)
info(name="ali",age=18)

def info(*args, **kwargs):
    print(kwargs)

def function1():
    print("function1")

def function2(a):
    print(a*a)

def function3():
    return "ssss"
"""
#Recursion
"""
def add(a):
    if a !=0:
        return a+add(a-1)
    else:
        return 0

x = int(input("Enter a number : "))
print ("sum = " , 3+add(2))

"""
#lambda expression
# variable name = lambda parameter  : body of function
"""
lambda1 = lambda  : print ("hello world")
"""
