import urllib.request
import json
import pymysql



dbServerName = "localhost"

dbUser = "root"

dbPassword = ""

dbName = "p5oc"

charSet = "utf8mb4"

connectionObject = pymysql.connect(db=dbName, user=dbUser, passwd=dbPassword, host=dbServerName)

# Test creation url

# category = resultat input utilisateur
produit: str = 'pizzas'

serviceurl = 'https://fr-en.openfoodfacts.org/category/'
# test : url = serviceurl + produit + '.json'

while True:
    if len(produit) < 1 : break

    url = serviceurl + produit + '/1.json'
    uh = urllib.request.urlopen(url)
    data = uh.read()
    #print ('Retrieved', len(data), 'characters')

    js = json.loads(data)

    x= js['products']

    for item in x:

        cursorObject = connectionObject.cursor()

        #name = item["product_name_fr"]
        #newname = name.replace("'", "\'")

        #print(item["product_name_fr"])
        insertStatement = "INSERT INTO produit (CategoryID, Name, Description, Link, Shop, EnergyValue) VALUES (1,' "+ item["product_name_fr"].replace("'", "\'") +" '  , 'blabla', 'www....', 'blabla', 890)"
        cursorObject.execute(insertStatement)
        print('\n')
        connectionObject.commit()


    break

