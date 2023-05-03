
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

mycursor.execute ("drop table if exists Felicità.data ")
#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS Felicità.data (
    Overall_rank INT,
    Country_or_region VARCHAR(30) NOT NULL,
    Score FLOAT,
    GDP_per_capita FLOAT,
    Social_support FLOAT,
    Healthy_life_expectancy FLOAT,
    Freedom_to_make_life_choices FLOAT,
    Generosity FLOAT,
    Perceptions_of_corruption FLOAT
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM Felicità.data")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./2019.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO Felicità.data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM Felicità.data")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)