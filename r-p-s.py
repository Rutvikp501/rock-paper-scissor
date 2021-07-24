# rock paper scissor 
import random
def game (comp,you):
    if comp==you:
        return None
    
        #check all possibilities when comp chose (r)
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
       #check all possibilities when comp chose (p)
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True  
        #check all possibilities when comp chose (g)
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True  

#to take random no or input from comp
print ("comp turn:: rock(r) paper(p) scisser(s)?\n ")
randno= random.randint(1, 3)
if randno==1:
    comp='r'
elif randno==2:
    comp='p'
elif randno==3:
    comp='s'
    
you= input("YOUR TURN:: rock(r) paper(p) scisser(s)?\n")
a = game(comp,you)
print (f"computer chose::{comp}")
print(f"you chose::{you}")

if comp==you:
    print("GAME IS TIE !")
elif a:
    print("YOU WIN THE GAME !")
else:
    print("you lose the game !")
