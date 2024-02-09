import math as mh
import turtle
screen = turtle.Screen()
pitagor = turtle.Turtle()
pitagor.hideturtle()
pitagor.color("black")
print("Добре дошли в калкулатор на питагорови тройки")
print("Въведете 1 за смятане по 2 катета")
print("Въведете 2 за смятане по катет и хипотенуза")
choice = int(input("Избор:"))
if choice == 1:
    katet1 = int(input("Дължина на първи катет:"))
    katet2 = int(input("Дължина на втори катет:"))
    hipotenusa = mh.sqrt(katet2**2+katet1**2)
    print('Хипотенузата е: ' + str(hipotenusa))
if choice == 2:
    katet1 = int(input("Дължина на първи катет:"))
    hipotenusa = int(input("Дължина на хипотенуза:"))
    katet2 = mh.sqrt(hipotenusa**2 - katet1**2)
    print('Другият катет е: ' + str(katet2))
lice = katet1*katet2/2
obikolka = katet1+katet2+hipotenusa
print("Лицето е: " + str(lice))
print("Обиколката е: " + str(obikolka))
orient = (90)
pitagor.forward(katet1*50)
pitagor.setheading(orient)
pitagor.forward(katet2*50)
pitagor.home()
