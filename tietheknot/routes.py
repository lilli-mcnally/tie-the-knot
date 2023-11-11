from flask import render_template
from tietheknot import app, db
from tietheknot.models import Checklist, Table, Guest

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/checklist")
def checklist():
    return render_template("checklist.html")

@app.route("/add_checklist_item", methods=["GET", "POST"])
def add_checklist_item():
    return render_template("add_checklist_item.html")


@app.route("/guests")
def guests():
    return render_template("guests.html")


@app.route("/table_plan")
def table_plan():
    return render_template("table_plan.html")


@app.route("/payments")
def payments():
    return render_template("payments.html")