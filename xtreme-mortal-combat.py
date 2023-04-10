import random
print("Welcome to the XTREME COMBAT")
spacename = " "
while True:
    p1name = input("please enter first player's name")
    if (p1name != spacename):
        print("Welcome", p1name)
        break
    else:
        print("Please enter first player's name again (none space)")
while True:
    p2name = input("Please enter second player's name ")
    if (p2name != spacename) and (p2name != p1name):
        print("Welcome", p2name)
        break
    else:
        print("Please enter second player's name again(none space and not same player's one name)")

print("Determining which player will go first...")
randomnamess = [p1name, p2name]
randomname = random.choice(randomnamess)
randomnamess.remove(randomname)
bb=randomnamess
aa=randomname
print(f"Coin toss result: {bb} starts first!")
def oyun_kodları():
    can1= 100
    can2= 100
    cizgi1= 50
    cizgi2= 50
    while True:
        print("------------", bb, "Attacks !!------------")
        print(bb, "HP [", can1, "]:", cizgi1 * "|",aa, "HP [",can2,"]:",cizgi2 * "|")
        M = int(input("Choose your attack magnitude between 1 and 50:"))
        while True:
            if M > 50 or M < 1:
                print("The attack magnitude must be between 1 and 50. ")
                M = int(input("Choose your attack magnitude between 1 and 50:"))
            else:
                break
        random.random()
        if random.random() > float((100-M) / 100):
            can2 = can2 - M
            cizgi2 = int(cizgi2 - (M / 2))
            print(aa , "hits", M, "damage")
            if can2 >= 1:
                print(bb, "HP [", can1, "]:", cizgi1 * "|", aa, "HP [",can2 ,"]:",cizgi2 * "|")

            if can2 < 1:
                print(bb, "HP [" ,can1, "]:", int(cizgi1 - (M / 2)) * "|" ,aa, "HP [0]:")
                print("#" * 67, "\n", "#" * 27, f"{bb} Wins!!", "#" * 27, "\n", "#" * 67)
                break
        else:
            print("missed for", bb)
            print(bb, "HP [", can1,"]", cizgi1 * "|", aa, "HP [", can2, "]:", cizgi2 * "|")

        print("------------", aa, "Attacks !!------------")
        print(bb, "HP [", can1, "]:", cizgi1 * "|", aa, "HP [", can2, "]:", cizgi2 * "|")
        M = int(input("Choose your attack magnitude between 1 and 50:"))
        while True:
            if M > 50 or M < 1:
                print("The attack magnitude must be between 1 and 50. ")
                M = int(input("Choose your attack magnitude between 1 and 50:"))
            else:
                break
        random.random()
        if random.random() > float((100 - M) / 100):
            can1 = can1 - M
            cizgi1 = int(cizgi1 - (M / 2))
            print(bb , "hits", M, "damage")
            if can1 >= 1:
                print(bb, "HP [", can1, "]:", cizgi1 * "|", aa, "HP [", can2, "]:", cizgi2 * "|")

            if can1 < 1:
                print(bb, "HP [0]:", aa, "HP [", can2, "]:", cizgi2 * "|")
                print("#" * 67, "\n", "#" * 27, f"{aa} Wins!!", "#" * 27, "\n", "#" * 67)
                break
        else:
            print("missed for", aa)
            print(bb, "HP [", can1, "]", cizgi1 * "|", aa, "HP [", can2, "]:", cizgi2 * "|")
def tekrar_oyna():
    again = input("Do you want to play another round (Yes or No)? :")
    while True:
        if again != "No" and again != "Yes":
            again = input("Do you want to play another round (Yes or No)? :")
        elif again == "Yes":
            oyun_kodları()
            break
        else:
            print("Thanks for playing! See you again")
            break
oyun_kodları()
tekrar_oyna()


