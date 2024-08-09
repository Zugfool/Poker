import random
import pandas as pd
import numpy as np
import turtle as t
import time

gruplar=["A","B","C","D"]
kartlar=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
tam_kartlar=[]

for i in gruplar:
    for j in kartlar:
        a=""
        a+=str(i)
        a+=str(j)
        tam_kartlar.append(a)

players=[]
timmy=t.Turtle()
timmy.pensize(6)
screen=t.Screen()
timmy.penup()
timmy.speed("fastest")
screen.screensize(600,450)
timmy.setpos(-300,200)

number= screen.numinput("","Enter the number of players: ")
for i in range(int(number)):
    name=screen.textinput("","Enter players name: ")
    players.append(name)
    
start= np.zeros(int(number))
start=start+50
start= list(start)
Points= pd.Series(start,players)
print("\n" + Points.to_string())

cards_drawn_list=[]

for j in players:
    timmy.penup()
    timmy.setx(-290)
    timmy.pendown()
    screen.clearscreen()
    timmy.penup()
    timmy.sety(200)
    timmy.pendown()
    timmy.write(j.capitalize() + " is playing", font=("Aria",30,"normal"))
    cards_drawn=[]
    for i in range(2):
        kart=random.choice(tam_kartlar)
        timmy.penup()
        timmy.seth(0)
        timmy.forward(120)
        timmy.sety(110)
        timmy.pendown()
        timmy.penup()
        timmy.sety(100)
        timmy.pendown()
        timmy.write(kart, font=("Aria",50,"normal"))
        cards_drawn.append(kart)
        tam_kartlar.remove(kart)
    print(cards_drawn)
    time.sleep(2)
    cards_drawn_list.append(cards_drawn)
print(cards_drawn_list)

orta=[]
timmy.setx(-500)
screen.clearscreen()
for i in range(5):
    kart=random.choice(tam_kartlar)
    timmy.penup()
    timmy.seth(0)
    timmy.forward(120)
    timmy.sety(110)
    timmy.pendown()
    for y in range(2):
        timmy.color("black")
        timmy.forward(110)
        timmy.left(90)
        timmy.forward(60)
        timmy.left(90)
    if kart[0]=="A" or kart[0]=="B":
        timmy.color("red")
    else:
        timmy.color("blue")
    timmy.penup()
    timmy.sety(100)
    timmy.pendown()
    timmy.write(kart[0:], font=("Aria",50,"normal"))
    orta.append(kart)
    tam_kartlar.remove(kart)
print("\n" + str(orta))
son_list=[]
straight_list=[]

for i in cards_drawn_list:
    son=[]
    full=[]
    straight=[]
    full=orta+i
    print(full)
    for j in range(len(full)):
        amount=0
        a=full[j][1:]
        c=full[j][0]
        straight.append(a)
        for x in range(len(full)):
            flush=0
            if full[j]==full[x]:
                pass
            elif j>x:
                pass
            else:
                b=full[x][1:]
                d=full[x][0]
                if a==b:
                    amount+=1
                    if amount==1:
                        son.append("2 of a kind")
                    elif amount==2:
                        son.append("3 of a kind")
                    elif amount==3:
                        son.append("4 of a kind")
                if c==d:
                    flush+=1
                    if flush==5:
                        son.append("Flush")
    son_list.append(son)
    straight_list.append(straight)

for i in son_list:
    print(i)
    for j in i:
        if j=="4 of a kind":
            for x in range(2):
                i.remove("3 of a kind")
            for x in range(3):
                i.remove("2 of a kind")
        elif j=="3 of a kind":
            for x in range(2):
                i.remove("2 of a kind")

for i in straight_list:
    for j in range(len(i)):
        w=i[j]
        if i[j]=="J":
            i[j]=11
        elif i[j]=="Q":
            i[j]=12
        elif i[j]=="K":
            i[j]=13
        elif i[j]=="A":
            i[j]=14
        else:
            i[j]=int(i[j])
    i.sort()
    
for i in son_list:
    if i.count("3 of a kind")==1 & i.count("2 of a kind")==1:
        i.append("Full House")

for i in range(len(straight_list)):
    on_a_roll=1
    for j in range(6):
        if straight_list[i][j+1]==straight_list[i][j]+1:
            on_a_roll+=1
        elif straight_list[i][j+1]==straight_list[i][j]:
            pass
        else:
            on_a_roll=1
        if on_a_roll==5:
            son_list[i].append("STRAIGHT")

timmy.penup()
timmy.setx(-300)
timmy.sety(300)
timmy.pendown()
screen.clearscreen()
#timmy.write(Points.to_string(), font=("Aria",50,"normal"))
print(son_list)
screen.clearscreen()
timmy.seth(270)

for i in son_list:
    if "STRAIGHT" in i:
        if "2 of a kind" in i:
            i.remove("2 of a kind")
        if "3 of a kind" in i:
            i.remove("3 of a kind")
        if "2 of a kind" in i:
            i.remove("2 of a kind")
        break
    if "Full House" in i:
        if "2 of a kind" in i:
            i.remove("2 of a kind")
        if "3 of a kind" in i:
            i.remove("3 of a kind")
        if "2 of a kind" in i:
            i.remove("2 of a kind")
        break
    if "Flush" in i:
        if "2 of a kind" in i:
            i.remove("2 of a kind")
        if "3 of a kind" in i:
            i.remove("3 of a kind")
        if "2 of a kind" in i:
            i.remove("2 of a kind")


for i in range(len(son_list)):
    timmy.forward(50)
    timmy.write(players[i], font=("Aria",40,"normal"))
    timmy.forward(50)
    timmy.write(str(son_list[i]), font=("Aria",40,"normal"))
timmy.hideturtle()
screen.exitonclick()