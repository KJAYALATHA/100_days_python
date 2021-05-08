#Randoomization and Array List [end task stone paper sissor]
#Random common methods
'''random()
randint(startvalue,endvalue)
randrange(startvalue,endvalue,2)It will display Even numbers
random.choice(listname)it select the random values from the list
random.suffle(listname)it shulle the random values from the list'''

#head or tail
import random
'''
game=random.randint(0,1)
print(game)
if(game==1):
    print("Heads")
else:
    print("Tails")'''

'''name=input("Give me anybody's name ,sepreated by a comma.").split(",")
#choice=random.choice(name)
choice=random.randint(0,len(name)-1)
print(name[choice],"is going to buy the meal today!")'''

row1=[1,2,3]
row2=[4,5,6]
row3=[7,8,9]
collection=[row1,row2,row3]

position=input("Where Do You want to put the treasure?")
print(position)
collection[int(position[0])][int(position[1])] = "X"

print(f"{row1}\n{row2}\n{row3}")
