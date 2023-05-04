from flask import render_template
from flask import Flask
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Felicità"
)
mycursor = mydb.cursor()


app = Flask(__name__)


@app.route('/test')
def hello():
    return render_template('hello.html', name='Fabio')



@app.route('/')

def unitList():
  #Esegui una Query per estrarre tutti i dati sulle unità dal DB. NB! Prima devi connetterti al DB
  mycursor.execute("SELECT * FROM data") 
  myresult = mycursor.fetchall()
  return render_template('hello.html', paesi=myresult)