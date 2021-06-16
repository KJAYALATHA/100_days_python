#Hangman game
import random
stages=['''
    +----+
    |    |
    0    |
   /|\   |
   / \   |
         |

==========
''','''
    +----+
    |    |
    0    |
   /|\   |
   /     |
         |
==========
''','''
    +----+
    |    |
    0    |
   /|\   |
         |
         |
==========
''','''
    +----+
    |    |
    0    |
   /|    |
         |
         |
==========
''','''
    +----+
    |    |
    0    | 
    |    |
         |
         |
==========
''','''
    +----+
    |    |
    0    |
         |
         |
         |
==========
''','''
    +----+
    |    |
         |
         |
         |
         |
==========
''']
display=[]
loosing=6
endgame= False
words=['apple','mango','orange']
randomword=random.choice(words)
length=len(randomword)
for i in range(length):
    display.append("_")
print(display)
print(randomword)
while endgame == False:
    u1=input("enter letter")
    if u1 in display:
        print(f'You have already guss this lrtter{u1}')
    for i in range(length):
        if u1==randomword[i]:
            display[i]=u1
    print(display)
    if u1 not in randomword:
        print(f'the letter not in the word you loosing yor lives')
        loosing -=1
        if loosing == 0:
            endgame = True
            print("You Loss!")
            
    if "_" not in display:
        endgame = True
        print("You Win!")
    print(stages[loosing])
 

    
