from flask import render_template
from tietheknot import app, db
from tietheknot.models import Checklist, Table, Guest

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")