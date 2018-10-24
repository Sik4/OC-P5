import urllib.request
import json
import pymysql
import re
from menu import __menu__
from menu import __cleartable__


dbServerName = "localhost"

dbUser = "root"

dbPassword = ""

dbName = "p5oc"

charSet = "utf8mb4"

connectionObject = pymysql.connect(db=dbName, user=dbUser, passwd=dbPassword, host=dbServerName)

# Test creation url
cleartable= __cleartable__()
produit = __menu__()

serviceurl = 'https://fr-en.openfoodfacts.org/category/'
# test : url = serviceurl + produit + '.json'


while True:
    if len(produit) < 1:
        break

    urls = [serviceurl + produit + '/{}.json'.format(p) for p in range(1, 10)]

    for url in urls:
        print(url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode('utf-8')
        # print ('Retrieved', len(data), 'characters')

        js = json.loads(data)

        x = js['products']

        for item in x:

            cursorObject = connectionObject.cursor()

            try:
                default = 'missing value'
                # name = item["product_name_fr"]
                name = item.get('product_name_fr', default)
                nametwo = item.get('ingredients_text', default)
                namethree = item["nutrition_grades_tags"]
                namefour = item["link"]
                # parcing all special characters
                newname = name.replace('œ', 'oe')
                enewname = re.escape(newname.strip())
                print(enewname)
                # replacing non problematic characters by their clean forms
                # '_'were around name of ingredients that should be in bold in CMS
                newnametwo = re.escape(nametwo.replace('_', ''))
                newnamethree = namethree[0]
                # intermediate verification
                # print(newname)
                # print(newnametwo)
                # parcing \% in final database before inserting datas
                insertStatement = "REPLACE INTO product (CategoryID, Name, Ingredient, Link,  EnergyValue) VALUES (" \
                                  "'1', '" + enewname + " ' ,'" + newnametwo.replace('\%', '%') + "' , '" + namefour +\
                                  "','" + newnamethree + "') "
                cursorObject.execute(insertStatement)
                # print('\n')

                connectionObject.commit()

            # finally:

                # connectionObject.close()

            except KeyError as e:
                # printing KeyError : careful, printing only one of the probably two ErrorS.
                print("KeyError on : ")
                print(str(e))
                # clean end of the loop when file is at the end
            else:
                continue

    sqlQuery = "SELECT DISTINCT ProduitID, Name, EnergyValue FROM product"

    # Fetch all the rows - for the SQL Query

    cursorObject.execute(sqlQuery)

    rows = cursorObject.fetchall()

    favorite = []
    for row in rows:
        # print(row)
        favorite.append(row)

    # creating the menu list
    print("\n Choisissez un produit : \n")
    key = []
    for cle, valeur, evalue in favorite:
        key.append(cle)
        print(cle, ": " + valeur, evalue)

    a = len(key)
    choice2 = 0
    try:
        choice2 = int(input("\n enter a choice between 1 and {} :  ".format(a)))
        print("\n")
    except ValueError:

        print("\n a number, like one...two....three...")
        print("\n")

    if choice2 not in range(1, a + 1):
        print("\n remove gloves before trying a number... ")
        print("\n")

    choix2 = favorite[choice2 - 1]
    produit2: str = choix2[1]
    eproduit2 = re.escape(produit2)
    print(eproduit2)

    # print(produit2)
    # return produit2
    print("Votre choix / Le choix le moins calorique")
    sqlQuery = "SELECT ProduitID, Name, EnergyValue FROM `product` WHERE Name = '" + eproduit2 + "' "\
               "UNION SELECT ProduitID, Name, EnergyValue FROM `product`WHERE CategoryID = 1 AND EnergyValue=(SELECT "\
               "MIN(EnergyValue) FROM `product`)"

    cursorObject.execute(sqlQuery)
    results = cursorObject.fetchall()
    sagesse = []
    nbrsolutions = 0
    for result in results:
        sagesse.append(result)
        nbrsolutions = nbrsolutions +1
        print(nbrsolutions - 1, result)

    choice3 = int(input("\n 0 pour garder votre ancien choix, entre 1 et  " +
                        "{} pour prendre le choix de la sagesse \n".format(nbrsolutions - 1)))

    if choice3 == 0:
        defchoice = sagesse[0]
        print(defchoice)
        insertStatement = "INSERT INTO substitute (ProduitID) VALUES ('" + str(defchoice[0]) + "')"
        cursorObject.execute(insertStatement)
        print("Votre choix est sauvegardé", defchoice)

    elif choice3 != 0:
        defchoice = sagesse[choice3]
        print(defchoice)
        insertStatement = "INSERT INTO substitute (ProduitID) VALUES ('" + str(defchoice[0]) + "')"
        cursorObject.execute(insertStatement)
        print("Votre choix est sauvegardé", defchoice)

    else:
        print("try again")

    exit()

