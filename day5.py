#find the average of heights in list
'''heights= input("Inputs a List Of Student Heights").split(" ")
print(heights)
length=len(heights)
print(length)
sum=0
for i in range(len(heights)):
    heights[i]=int(heights[i])
    sum=sum+heights[i]
print(sum)
total=sum/length
print(round(total))'''

#find the largets nuber in the list list
'''heights= input("Inputs a List Of Student Heights").split(" ")
highestscore=0
for i in heights:
    i=int(i)
    if(i>highestscore):
        highestscore=i
print(highestscore)'''

#find the Even numbers sum
'''sum=0
for i in range(0,101,2):
    sum=sum+i
print(sum)'''
#number to print 1 to 100 instead number divisble by 3 it print fizz ,it divisible by
#5 it print buzz it divisible by both print Fizz BuZZ
'''for i in range(1,100,1):
    if(i%3==0)and(i%5==0):
        print("FizzBuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print(i)'''
#Pass Word Generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
         'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
         'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
         'V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0',]
symbols=['~','@','#','$','%','^','&','*','(',')',]

print("WELCOME TO THE PYPASSWORD GENERATOR")
alpha=int(input("How many letters would you like in your password?"))
special=int(input("How many symbols would you like in your password?"))
num=int(input("How many numbers would you like in your password?"))
password=[]
for i in range(alpha):
    password.append(random.choice(letters))
for i in range(special):
    password.append(random.choice(symbols))
for i in range(num):
    password.append(random.choice(numbers))

random.shuffle(password)
passwordlist=""
for i in password:
    passwordlist+=i
print(passwordlist)
    


                   
