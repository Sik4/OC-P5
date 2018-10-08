import pymysql

# WARNING You have to put the categories you want to work with BY HAND line 80 AFTER testing to see if they exist in
# database

# Create a connection object


dbServerName = "localhost"

dbUser = "root"

dbPassword = ""

dbName = "p5oc"

charSet = "utf8mb4"

connectionObject = pymysql.connect(db=dbName, user=dbUser, passwd=dbPassword, host=dbServerName)

try:

    # Create a cursor object

    cursorObject = connectionObject.cursor()

    # SQL string to create a MySQL table

    # dropping existing tables (reset program)

    cursorObject.execute("DROP TABLE IF EXISTS `category`;")
    cursorObject.execute("DROP TABLE IF EXISTS `product`;")
    cursorObject.execute("DROP TABLE IF EXISTS `substitute`;")

    # creating tables. be careful with data types
    sqlCreateTableCommand1 = "CREATE TABLE IF NOT EXISTS `category` (  `CategoryID` " \
                             "tinyint(4) NOT NULL AUTO_INCREMENT,  `ParentID` tinyint(4) NOT NULL,  `Name` varchar(" \
                             "255) CHARACTER SET utf8 NOT NULL, PRIMARY KEY (`CategoryID`)) "

    sqlCreateTableCommand2 = "CREATE TABLE IF NOT EXISTS `product` ( `ProduitID` " \
                             "smallint(7) NOT NULL AUTO_INCREMENT,`CategoryID` tinyint(3) NOT NULL,`Name` varchar(255) "\
                             "COLLATE utf8_unicode_ci NOT NULL,`Ingredient` text COLLATE utf8_unicode_ci NOT NULL," \
                             "`Link` varchar(255) COLLATE utf8_unicode_ci NOT NULL,`EnergyValue` varchar(255)" \
                             "COLLATE utf8_unicode_ci NOT NULL, PRIMARY KEY (`ProduitID`)) "

    sqlCreateTableCommand3 = "CREATE TABLE IF NOT EXISTS `substitute` (`SubstitutID` tinyint(3) NOT NULL " \
                             "AUTO_INCREMENT,`ProduitID` tinyint(3) NOT NULL, PRIMARY KEY (`SubstitutID`))"

    # Execute the sqlQuery

    cursorObject.execute(sqlCreateTableCommand1)
    cursorObject.execute(sqlCreateTableCommand2)
    cursorObject.execute(sqlCreateTableCommand3)

    cursorObject.execute(
        "ALTER TABLE `product`  ADD CONSTRAINT `FK_CategoryID` FOREIGN KEY (`CategoryID`) REFERENCES `category` ("
        "`CategoryID`);")

    cursorObject.execute(
        "ALTER TABLE `substitute`  ADD CONSTRAINT `FK_ProduitID` FOREIGN KEY (`ProduitID`) REFERENCES `product` ("
        "`ProduitID`);")

    # List the tables using SQL command

    sqlShowTablesCommand = "show tables"

    # Execute the SQL command

    cursorObject.execute(sqlShowTablesCommand)

    # Fetch all the rows - from the command output

    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

    # Insert rows into the MySQL Table
    # inserting categories previously tested manually

    insertStatement = "INSERT INTO Category (CategoryID, ParentID, Name) VALUES (1,1,\"Pizzas\"), (2,1,\"Chips\")," \
                      " (3,2,\"Gateaux\"), (4,2,\"Teas\"), (5,3, \"fish\")"

    # Popcorn works fine

    cursorObject.execute(insertStatement)

    # SQL Query to retrieve the rows

    sqlQuery = "select * from category"

    # Fetch all the rows - for the SQL Query

    cursorObject.execute(sqlQuery)

    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

    connectionObject.commit()

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionObject.close()
