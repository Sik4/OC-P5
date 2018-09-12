import pymysql

# coding: utf-8

"""OC P5"""
"""Files : """

# definition of function transforming category table into menu


def __menu__():
    # connect to database :
    dbServerName = "localhost"
    dbUser = "root"
    dbPassword = ""
    dbName = "p5oc"
    charSet = "utf8mb4"

    connectionObject = pymysql.connect(db=dbName, user=dbUser, passwd=dbPassword, host=dbServerName)

    print("\n This program will help you choose an healthy meal")

    cursorObject = connectionObject.cursor()

    # fetching datas to create the menu

    sqlQuery = "SELECT CategoryID, Name FROM category"

    cursorObject.execute(sqlQuery)
    rows = cursorObject.fetchall()

    menu = []

    for row in rows:
        menu.append(row)

    # creating the menu list

    key = []
    for cle, valeur in menu:
        key.append(cle)
        print(cle, ": " + valeur)

    a = len(key)
    choice = 0

    try:
        choice = int(input("\n enter a choice between 1 and {} :  ".format(a)))
        print("\n")

    except ValueError:

        print("\n a number, like one...two....three...")
        print("\n")
        exit()

    if choice not in range(1, a + 1):
        print("\n remove gloves before trying a number... ")
        print("\n")
        exit()

    choix = menu[choice - 1]
    produit: str = choix[1]

    print(produit)
    return produit
