 
# string 

print("hello world")
print("my name is abhishek kr. singh")
print("i am 21 years old")

# int

a = 3
b = 5
sum = a+b

# arithemetic operator

print(a*b)
print(a-b)
print(a/b)
print(sum)
print(a%b)
print(a**b)

# relational operator

print(a==b) #equal to
print(a!=b) #not equal to 
print(a<b)  #lower then
print(a>b)  #greter then
print(a<=b) #lower then equal to
print(a>=b) #greater then equal to

# assignment operators

num = 50
num+= 50
print(num)
num1 = 20
num1 -= 20
print(num1)
num2 = 10
num2 *= 6
print(num2)
num3 = 60
num3 /= 6
print(num3)
num4 = 45
num4 %= 4
print(num4)
num5 = 12
num5 **= 2
print(num5)

# logical operator

a1 = 35
b1 = 45
print(not False)
print(not (a1<b1))
print(not (a1>b1))

a2 = True
b2 = True
print(a2 and b2)

a2 = True
b2 = False
print(a2 and b2)
print(a2 or b2)

# type conversion 

a = "3"
b = 2.5
c = int("3")
print(b+c)

a = "3"
b = 2.5
c = float("3")
print(b+c)

# input in python 

name = input("enter you name: ") #result for input is always a string 
print("welcome", name)

name1 = input("enter you name:" )
age = input("enter you age: ")
marks = input("enter your marks: ")
print("welcome", name1)
print("age", age)
print("marks", marks)