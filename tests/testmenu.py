import pymysql

dbServerName = "localhost"

dbUser = "root"

dbPassword = ""

dbName = "p5oc"

charSet = "utf8mb4"

connectionObject = pymysql.connect(db=dbName, user=dbUser, passwd=dbPassword, host=dbServerName)


cursorObject = connectionObject.cursor()

sqlQuery = "SELECT CategoryID, Name FROM category"

# Fetch all the rows - for the SQL Query

cursorObject.execute(sqlQuery)
rows = cursorObject.fetchall()

menu =[]

for row in rows:
    menu.append(row)
    print(row)

print(menu)
