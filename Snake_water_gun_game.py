import random as rd

st="Eeshan Bablani Presents"
print(st.center(50,"_"))
st1= "THE SNAKE-WATER-GAME"
print("\n",st1.center(50,"-"))
print("\n","Your competitor is your own computer !!")
print("\n","Enjoy The game ")
print("\n","If you feel defeated please don't come to me 🤣🤣")

attributes={'Draw': 0,'Win': 1, 'Lose': -1}
l1=["Snake","Water","Gun"]

def onetime():
    i=-1
    while (i<0):
        player1=input("Choose between snake,water,gun : ")
        computer=rd.choice(l1)
        if player1.capitalize()==computer :
            print(f"Your result is Draw and your score is {attributes.get('Draw')}")
            break
        
        elif player1.capitalize()==l1[0] and computer.capitalize()==l1[1]:
            print(f"Computer wins and your score is {attributes.get('Lose')}")
            break
        
        elif player1.capitalize()==l1[0] and computer.capitalize()==l1[2]:
            print(f"Computer wins and your score is {attributes.get('Lose')}")
            break
        
        elif player1.capitalize()==l1[1] and computer.capitalize()==l1[0] :
            print(f"You win and your score is {attributes.get('Win')}")
            break
        
        elif player1.capitalize()==l1[1] and computer.capitalize()==l1[2] :
            print(f"You win and your score is {attributes.get('Win')}")
            break
        
        elif player1.capitalize()==l1[2] and computer.capitalize()==l1[0] :
            print(f"You win and your score is {attributes.get('Win')}")
            break
        
        elif player1.capitalize()==l1[2] and computer.capitalize()==l1[1]:
            print(f"Computer wins and your score is {attributes.get('Lose')}")
            break
        else :
            raise Exception("Dont you have eyes even 🤣🤣??Type cautiously you fool")
def multipletime():
    w=int(input("for how many times you want to play :"))
    final_score=0
    for i in range(0,w):
        player1=input("\n Choose between snake,water,gun : ")
        computer=rd.choice(l1)
        if player1.capitalize()==computer :
            print(f"Your result is Draw and your score is {attributes.get('Draw')}")
            final_score=final_score+0
        
        elif player1.capitalize()==l1[0] and computer.capitalize()==l1[1]:
            print(f"Computer wins and your score is {attributes.get('Lose')}")
            final_score=final_score-1
        
        elif player1.capitalize()==l1[0] and computer.capitalize()==l1[2]:
            print(f"Computer wins and your score is {attributes.get('Lose')}")
            final_score=final_score-1
        
        elif player1.capitalize()==l1[1] and computer.capitalize()==l1[0] :
            print(f"You win and your score is {attributes.get('Win')}")
            final_score=final_score+1
            
        elif player1.capitalize()==l1[1] and computer.capitalize()==l1[2] :
            print(f"You win and your score is {attributes.get('Win')}")
            final_score=final_score+1
        
        elif player1.capitalize()==l1[2] and computer.capitalize()==l1[0] :
            print(f"You win and your score is {attributes.get('Win')}")
            final_score=final_score+1
        
        elif player1.capitalize()==l1[2] and computer.capitalize()==l1[1]:
            print(f"Computer wins and your score is {attributes.get('Lose')}")
            final_score=final_score-1
        
        else :
            raise Exception("\n Don't you have eyes even 😂😂??Type cautiously you fool")
    print(f"\n So after {w} games your score is : {final_score}")
            
x=input("Are You ready to play this game? :")

if x.lower()=="yes" :
    print("\n","So you want to get defeated single time or multiple times?")
    z=int(input("\n press 1 for multiple time  \n press 2 for single time \n Your input : "))
    if z==1 :
        multipletime()
    else:
        onetime()
elif x.lower()=='no':
    print("Proven Loser you are. GO your moma is calling you😂😂")
else :
    raise Exception("Don't you have eyes or what ?? \n say yes or no")
