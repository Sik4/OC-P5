#coding: utf-8

"""OC P5"""
"""Files : """


print("\n This program will help you choose between red pill and blue pill")


#creating the menu list
#testing with fake menu


menu = {"1" : "Pizza" ,  "2" : "Chips", "3" :"Chaussettes"}

key = []
for cle,valeur in menu.items():
    key.append(cle)
    print (cle, valeur)

a = len(key)
choice = 0
while True:
    try:
        choice = int(input("\n enter a choice between 1 and {} :  ".format(a)))
        print("\n")
    except ValueError:

        print("\n a number, like one...two....three...")
        print("\n")
        continue

    if choice not in range(1,a+1):
        print("\n remove gloves before trying a number... ")
        print("\n")
        continue
    else:
        break

print ("\n you chose", choice)

