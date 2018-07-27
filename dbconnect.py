import pymysql

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

    cursorObject.execute("DROP TABLE IF EXISTS `category`;")
    cursorObject.execute("DROP TABLE IF EXISTS `produit`;")
    cursorObject.execute("DROP TABLE IF EXISTS `substitut`;")


    sqlCreateTableCommand1 = "CREATE TABLE IF NOT EXISTS `category` (  `CategoryID` " \
                             "tinyint(4) NOT NULL AUTO_INCREMENT,  `ParentID` tinyint(4) NOT NULL,  `Name` varchar(" \
                             "40) CHARACTER SET utf8 NOT NULL, PRIMARY KEY (`CategoryID`)) "

    sqlCreateTableCommand2 = "CREATE TABLE IF NOT EXISTS `produit` ( `ProduitID` " \
                             "tinyint(3) NOT NULL AUTO_INCREMENT,`CategoryID` tinyint(3) NOT NULL,`Name` varchar(40) " \
                             "COLLATE utf8_unicode_ci NOT NULL,`Description` text COLLATE utf8_unicode_ci NOT NULL," \
                             "`Link` varchar(255) COLLATE utf8_unicode_ci NOT NULL,`Shop` varchar(40) COLLATE "\
                             "utf8_unicode_ci NOT NULL,`EnergyValue` smallint(5) NOT NULL, "  \
                             "PRIMARY KEY (`ProduitID`)) "


    sqlCreateTableCommand3 = "CREATE TABLE IF NOT EXISTS `substitut` (`SubstitutID` tinyint(3) NOT NULL " \
                             "AUTO_INCREMENT,`ProduitID` tinyint(3) NOT NULL,`Name` varchar(40) COLLATE " \
                             "utf8_unicode_ci NOT NULL,`Description` text COLLATE utf8_unicode_ci NOT NULL," \
                             "`Link` varchar(255) COLLATE utf8_unicode_ci NOT NULL,`Shop` varchar(40) COLLATE " \
                             "utf8_unicode_ci NOT NULL,`EnergyValue` smallint(5) NOT NULL, "\
                             "PRIMARY KEY (`SubstitutID`))"

    # Execute the sqlQuery

    cursorObject.execute(sqlCreateTableCommand1)
    cursorObject.execute(sqlCreateTableCommand2)
    cursorObject.execute(sqlCreateTableCommand3)

    cursorObject.execute("ALTER TABLE `produit`  ADD CONSTRAINT `FK_CategoryID` FOREIGN KEY (`CategoryID`) REFERENCES `category` (`CategoryID`);")

    cursorObject.execute("ALTER TABLE `substitut`  ADD CONSTRAINT `FK_ProduitID` FOREIGN KEY (`ProduitID`) REFERENCES `produit` (`ProduitID`);")


    # List the tables using SQL command

    sqlShowTablesCommand = "show tables"

    # Execute the SQL command

    cursorObject.execute(sqlShowTablesCommand)

    # Fetch all the rows - from the command output

    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

    # Insert rows into the MySQL Table

    #insertStatement = "INSERT INTO Category (CategoryID, ParentID, Name) VALUES (1,2,\"Einstein\")"

    #cursorObject.execute(insertStatement)

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
