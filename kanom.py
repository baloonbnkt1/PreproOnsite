"Onsite Prepro"
def main():
    "ppp"
    money = int(input())
    water = int(input())
    sna1 = int(input())
    sna2 = int(input())
    sna3 = int(input())
    ton = money-water
    if ton % 3 == 0:
        sn1 = sna1*10
        ton -= sna1*10
    elif ton % 3 == 1:
        sn1 = sna1*15
        ton -= sna1*15
    else:
        sn1 = sna1*20
        ton -= sna1*20
    if ton % 3 == 0:
        sn2 = sna2*12
        ton -= sna2*12
    elif ton % 3 == 1:
        sn2 = sna2*15
        ton -= sna2*15
    else:
        sn2 = sna2*18
        ton -= sna2*18
    if ton % 3 == 0:
        sn3 = sna3*5
        ton -= sna3*5
    elif ton % 3 == 1:
        sn3 = sna3*7
        ton -= sna3*7
    else:
        sn3 = sna3*9
        ton -= sna3*9
    if ton < 0:
        print("Now you have %d left." %money)
        print("You don't have enough money!")
    else:
        print("Now you have %d left." %ton)
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht" %(sn1))
        print("Snack number 2: %d baht" %(sn2))
        print("Snack number 3: %d baht" %(sn3))
main()
