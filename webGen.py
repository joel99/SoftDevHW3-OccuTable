from flask import Flask, render_template
import random
from utils import occupation

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('home.html', title = "Home", head = "Directory", links = ['/occupation'])

@app.route("/occupation")
def occupationPage():   
    header = "Occupation Database"
    return render_template('occupation.html', title = "Occupations", head = header, links = ['/'], table = occupation.getD(), randChoice = occupation.randSelect())

if __name__ == "__main__":
    app.debug = True
    app.run()
