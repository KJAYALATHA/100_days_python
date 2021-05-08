# water level above 80cm water drain otherwise continue
# theme park height above 120cm con ride otherwin cant drive //height = true ,age <7 55rs >7 and <40 70 rs otherwise 100 rs
#odd or even

'''height=float(input("enter a height"))
weight=float(input("enter a weight"))
bmi=(weight//height**2)
print(bmi)
if(bmi<18.5):
    print("below normal")
elif(bmi >= 18.5 and bmi<25):
    print("normal")
elif(bmi >= 25 and bmi<30):
    print("overweight")
elif(bmi >= 30 and bmi<35):
    print("class 31obesety")
elif(bmi >= 35 and bmi<40):
    print("class 2 obesety")
elif(bmi >= 40):
    print("class 3 obesety")
elif(bmi <=0):
    print("invalid bmi")'''

#year = int(input("Enter Year: "))

'''# Leap Year Check[elif]
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# neseted if
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
        else:
            print(year, "is not a Leap Year")
    else:
        print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")'''

#rooler la photo
'''bill=0
size=input("What size pizza do you want? S, M, or L ").upper()
if(size =="S"):
    bill +=15
elif(size =="M"):
    bill += 20
else:
    bill = +25
add_pep= input("Do you want pepperoni? Y or N ").upper()
if(size =="S" and add_pep == "Y"):
    bill = bill+2
else:
    bill = bill+3
chesse= input("Do you want extra cheese? Y or N ").upper()
if(chesse == "Y"):
    bill = bill+1
    print("Your Final bill is: $",bill)
else:
    print("Your Final bill is: $",bill)'''

#Love Calculator

'''your=input("enter yours name ").lower()
their=input("enter their name ").lower()
love=your+their
print(love)
t=love.count("t")
r=love.count("r")
u=love.count("u")
e=love.count("e")
l=love.count("l")
o=love.count("o")
v=love.count("v")
e=love.count("e")
connect1=t+r+u+e
connect2=l+o+v+e
print(connect1)
print(connect2)
pair=str(connect1)+str(connect2)
if(int(pair) <10 or int(pair)>90):
    print(f"yourr score is {pair} you go toghther like coke and mentos")
elif(int(pair) > 40 and int(pair) <50):
    print(f"yourr score is {pair} your are alright toghther")
else:
    print(f"yourr score is {pair}")'''

#Treasure Finding
print("Welcome to Treasure Island.Your mission is to Find the tresure.")
way=input('You are at the crossroad,Where do you want to go?Type "left" or "right"')


if(way == "left"):
    thing=input("You come to a lake.there is an island in the middle of the lake. type 'wait' to wait for a boat.type 'swim' to swim across.")
    if(thing == "wait"):
        colour=input(""):
            if(colour == "yellow"):
                print("you Win")
            else:
                print("Game Over")
    else:
        print("game Over")
else:
    print("game Over")
    

