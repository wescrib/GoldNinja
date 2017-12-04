from flask import Flask, render_template, redirect, flash
from random import *
import time

app = Flask(__name__)
app.secret_key="ive got all the coupons"

@app.route("/")
def index():

    if not "gold" in session:
        session["gold"] = 0
    if not "desc" in session:
        session["desc"] = ""
    return render_template("index.html", session["gold"], session["desc"])

@app.route("/farm", method =["POST"])
def farm():
    temp_gold = random.randomrange(10,20)
    session["gold"] += temp_gold
    session["desc"] += ("You have gained", temp_gold,"from the farm, at", time.clock())
    return redirect("/")

@app.route("/cave", method =["POST"])
def cave():
    temp_gold = random.randomrange(5,10)
    session["gold"] += temp_gold
    session["desc"] += ("You have gained", temp_gold,"from the cave, at", time.clock())
    return redirect("/")

@app.route("/house", method =["POST"])
def house():
    temp_gold = random.randomrange(2,5)
    session["gold"] += temp_gold
    session["desc"] += ("You have gained", temp_gold,"from the house, at", time.clock())
    return redirect("/")

@app.route("/casino", method =["POST"])
def casino():
    temp_gold = random.randomrange(-50,50)
    session["gold"] += temp_gold
    if temp_gold > 0:
        session["desc"] += ("You have gained", temp_gold,"from the casino, at", time.clock())
    else:
        session["desc"] += ("You have lost", temp_gold,"from the casino, at", time.clock())
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    session["gold"] = 0
    session["desc"] = ""
    return redirect("/")
@app.run(debug=True)