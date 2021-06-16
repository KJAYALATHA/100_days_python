n=[]
end_of_game= True
def opt():
    for i in range(9):
        print(n[i],end=" ")
        if(i==2 or i==5 or i==8):
            print()
for i in range(9):
    n.append(i+1)
opt()
def success(endvalue):
    if((n[0] and n[1] and n[2] == "x")or (n[3] and n[4]and n[5] == "x") or (n[6] and n[7]and n[8] == "x") or
           (n[0] and n[3]and n[6] == "x") or(n[1] and n[4]and n[7] == "x") 
           or(n[2] and n[5]and n[8] == "x") or(n[0] and n[4]and n[8] == "x")or(n[2] and n[4]and n[6] == "x")):
       
        return "X"
    elif( (n[0] and n[1] and n[2] == "O")or (n[3] and n[4] and n[5] == "O") or
           (n[6] and n[7] and n[8] == "O") or (n[0] and n[3] and n[6] == "O") or (n[1] and n[4] and n[7] == "O")
           or(n[2] and n[5] and n[8] == "O")or (n[0] and n[4] and n[8] == "O")or(n[2] and n[4]and n[6] == "O")):
      
        return "O"
    else:
        if(endvalue==8):
            return "draw"


for i in range(9):
    if(i%2 != 0):
        user=int(input("enter ur x choice"))
        n[user-1]="x"
        opt()
    else:
        user=int(input("enter ur O choice"))
        n[user-1]="O"
        opt()
        print(n)
    if(success(i)=='x' or success(i) == "O"):
        print(f'{success(i)} is win')
        break
    
           
     
        
        
    


        
    


        
