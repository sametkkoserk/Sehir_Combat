print("hello gamers")
player1=input("name of player one:")
while player1==(""):
    print("name cannot be empty:")
    player1=input("name of player one:")
hero1="h1"
power1=100
health1=100
player2=input("name of player two:")
while player1==player2:
    print("you have to write different name:")
    player2=input("name of player two:")
while player2==(""):
    print("name cannot be empty:")
    player2=input("name of player two:")
hero2="h2"
power2=100
health2=100

class hero():
    def __init__(self,power=100,health=10):

        self.p= power
        self.h= health
Ensar_Gul=hero(150,300)
Ahmet_Bulut=hero(100,400)
Ahmet_Bulut=hero(125,350)
print("1-Ensar Gül\npower=150\nhealth=300")
print("2-Ahmet Bulut\npower=100\nhealth=400")
print("3-Ali Çakmak\npower=125\nhealth=350")

x=int(input(player1+" choose your hero's number:"))
while x<1 or x>3 :
    x=int(input("you have to choose 1 or 2 or 3:"))
if(x==1):
    hero1="Ensar Gül"
    power1=Ensar_Gul.p
    health1=Ensar_Gul.h
elif(x==2):
    hero1="Ahmet Bulut"
    power1=Ahmet_Bulut.p
    health1=Ahmet_Bulut.h
elif(x==3):
    hero1="Ali Çakmak"
    power1=Ahmet_Bulut.p
    health1=Ahmet_Bulut.h
y=int(input(player2+" choose your hero's number:"))
while y<1 or y>3:
    y=int(input("you have to choose 1 or 2 or 3:"))
if(y==1):
    hero2="Ensar Gül"
    power2=Ensar_Gul.p
    health2=Ensar_Gul.h
elif(y==2):
    hero2="Ahmet Bulut"
    power2=Ahmet_Bulut.p
    health2=Ahmet_Bulut.h
elif(y==3):
    hero2="Ali Çakmak"
    power2=Ahmet_Bulut.p
    health2=Ahmet_Bulut.h

import random
a=random.random()
if(a<=0.5):
    k=1
    print("player1 first")
else:
    k=0
    print("player2 first")
while health1>0 and health2>0:
    print("1-attack\n2-health")
    if k==1:
        a=int(input(player1+" choose your attack's number:"))
        while a < 1 or a > 2:
            a = int(input("you have to choose 1 or 2 :"))
        if a==1:
            import random
            health2=health2-(power1*random.uniform(0.5,1)/2)
        elif a==2:
            import random
            health1=health1+(power1*random.uniform(0.5,1)/2)
        print(hero1,"'s health is ",health1)
        print(hero2,"'s health is ",health2)
        if health1 <= 0.0:
            break
            print(player2 + " won")
        elif health2 <= 0.0:
            break
            print(player1 + " won")
        a2 = int(input(player2 + " choose your attack's number:"))
        while a2 < 1 or a2 > 2:
            a2 = int(input("you have to choose 1 or 2 :"))
        if a2 == 1:
            import random
            a = random.uniform(0.5, 1)
            health1 = health1 - (power2 * a / 2)
        elif a2 == 2:
            import random

            health2 = health2 + (power2 * random.uniform(0.5, 1) / 2)
        """
        print(hero1,"'s health is ",health1)
        print(hero2,"'s health is ",health2)
        """
    else:
        a2=int(input(player2+" choose your attack's number:"))
        while a2 < 1 or a2 > 2:
            a2 = int(input("you have to choose 1 or 2 :"))
        if a2==1:
            import random
            health1=health1-(power2*random.uniform(0.5,1)/2)
        elif a2==2:
            import random
            health2=health2+(power2*random.uniform(0.5,1)/2)
        print(hero1,"'s health is ",health1)
        print(hero2,"'s health is ",health2)
        if health1 <= 0.0:
            break
            print(player2 + " won")
        elif health2 <= 0.0:
            break
            print(player1 + " won")
        a = int(input(player1 + " choose your attack's number:"))
        while a < 1 or a > 2:
            a = int(input("you have to choose 1 or 2 :"))
        if a == 1:
            import random
            a = random.uniform(0.5, 1)
            health2 = health2 - (power2 * a / 2)
        elif a == 2:
            import random

            health1 = health1 + (power2 * random.uniform(0.5, 1) / 2)
    print(player1+"'s health is ",health1)
    print(player2+"'s health is ",health2)
"""    if health1 <= 0.0:
        break
        print(player2 + " won")
    elif health2 <= 0.0:
        break
        print(player1 + " won")
    if k==0:
        a2=int(input(hero2+" choose your attack's number:"))
        while a2<1 or a2>2 :
            a2=int(input("you have to choose 1 or 2 :"))
        if a2==1:
            import random
            a=random.uniform(0.5,1)
            health2=health2-(power2*a/2)
        elif a2==2:
            import random
            health1=health1+(power2*random.uniform(0.5,1)/2)

        print(player1,"'s health is ",health1)
        print(player2,"'s health is ",health2)

    else:
        a2=int(input(hero2+" choose your attack's number:"))
        while a2 < 1 or a2 > 2:
            a2 = int(input("you have to choose 1 or 2 :"))
        if a2==1:
            import random
            health1=health1-(power2*random.uniform(0.5,1)/2)
        elif a2==2:
            import random
            health2=health2+(power2*random.uniform(0.5,1)/2)
    print(player1,"'s health is ",health1)
    print(player2,"'s health is ",health2)"""
if  health1<=0.0:
    print(player2+" won")
elif health2<=0.0:
    print(player1+" won")