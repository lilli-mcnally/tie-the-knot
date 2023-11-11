from flask import render_template, request, redirect, url_for
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
    checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
    return render_template("checklist.html", checklist_items=checklist_items)

@app.route("/add_checklist_item", methods=["GET", "POST"])
def add_checklist_item():
    if request.method == "POST":
            checklist_item = Checklist(
                checklist_name=request.form.get("checklist_name"),
                checklist_notes=request.form.get("checklist_notes"),
                checklist_date=request.form.get("checklist_date"),
                checklist_payment=bool(True if request.form.get("checklist_payment") else False)
            )
            db.session.add(checklist_item)
            db.session.commit()
            return redirect(url_for("checklist"))
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