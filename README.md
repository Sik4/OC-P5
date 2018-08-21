# OC-P5

How to use the application : 

- Create a db following those rules : 
dbServerName = "localhost"
    dbUser = "root"
    dbPassword = ""
    dbName = "p5oc"
    charSet = "utf8mb4"
    
- Launch dbconnect.py
to create the tables 

- Launch main.py
follow instructions and enjoy

Plan of the application : 

- Interface Function
Ask a question, return alarm if answer is not standardized 
Question : letting the choice of finding every category of aliment or list ? 

- Function that will form URL with the answers of the user
If user input is standardized, form URL using template : 
https://fr-en.openfoodfacts.org/category/answer

- Retrieve the datas from the API, sort them and export them as a json file
Clean the datas : looking for : 
Name : product_name_fr
Ingredient : ingredients_text_fr or ingredients_text_debug
Link : link
Shop :
Energy : energy_value



- Function that will put the json file in the DB
Auto increment ID key. If list asked by user, use ID key is used as answer

- Comparaison of the datas, and finding the right answer
Comparaison of energy_value, take min and return to user. 

- Display of the solution to the user
