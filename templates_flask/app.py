from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html', name='Fabio')



@app.route('/units').

def unitList():
  Esegui una Query per estrarre tutti i dati sulle unità dal DB. NB! Prima devi connetterti al DB
  mycursor.execute("SELECT FROM Clash_Unit") myresult = mycursor.fetchall()
  return render_template('clash_units.html', units=myresult)