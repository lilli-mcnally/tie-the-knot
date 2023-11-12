from flask import render_template, request, redirect, url_for, flash
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
    print("one")
    if request.method == "POST":
        print("two")
        checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
        print("three")
        for x in checklist_items:
            print("four")
            if request.form.get("checklist_name") == x:
                print("5")
                flash("Checklist name already taken")
                print("6")
                return redirect(url_for("add_checklist_item"))
                print("7")
            else:
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

@app.route("/edit_checklist_item/<int:checklist_item_id>", methods=["GET", "POST"])
def edit_checklist_item(checklist_item_id):
    checklist_item = Checklist.query.get_or_404(checklist_item_id)
    if request.method == "POST":
        checklist_item.checklist_name = request.form.get("checklist_name")
        checklist_item.checklist_notes = request.form.get("checklist_notes")
        checklist_item.checklist_date = request.form.get("checklist_date")
        checklist_item.checklist_payment = bool(True if request.form.get("checklist_payment") else False)
        db.session.commit()
        return redirect(url_for("checklist"))
    return render_template("edit_checklist_item.html", checklist_item=checklist_item)

@app.route("/delete_checklist_item/<int:checklist_item_id>")
def delete_checklist_item(checklist_item_id):
    checklist_item = Checklist.query.get_or_404(checklist_item_id)
    db.session.delete(checklist_item)
    db.session.commit()
    return redirect(url_for("checklist"))

@app.route("/guests")
def guests():
    return render_template("guests.html")

@app.route("/add_guests", methods=["GET", "POST"])
def add_guests():
    if request.method == "POST":
        guest = Guest(
            guest_name=request.form.get("guest_name"),
            guest_notes=request.form.get("guest_notes"),    
            table_number=request.form.get("table_number")
        )
        db.session.add(guest)
        db.session.commit()
        return redirect(url_for("guests"))
    return render_template("add_guests.html")


@app.route("/table_plan")
def table_plan():
    return render_template("table_plan.html")


@app.route("/payments")
def payments():
    checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
    return render_template("payments.html", checklist_items=checklist_items)