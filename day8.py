alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','n','o','p',
          'q','r','s','t','u','v','w','x','y','z',]
direction=input("type 'encode' to encypt or 'decode' to decrypt \n")
text = input("enter a message \n").lower()
shift=int(input("Type Shift number /n"))
def encrypt(text,amount):
    cipher=''
    for i in text:
        position=alphabet.index(i)
        new_position=position + amount
        letter = alphabet[new_position]
        cipher+=letter
    print(cipher)
encrypt(text,shift+1)
        
    
