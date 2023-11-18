from flask import render_template, request, redirect, url_for, flash
from tietheknot import app, db
from tietheknot.models import Checklist, Table, Guest

# Main pages
@app.route("/")
def home():
    return render_template("base.html")

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


# Checklist Pages
@app.route("/checklist")
def checklist():
    checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
    return render_template("checklist.html", checklist_items=checklist_items)

@app.route("/add_checklist_item", methods=["GET", "POST"])
def add_checklist_item():
    if request.method == "POST":
        # Gets the string from in the checklist name box
        new_checklist_name = request.form.get('checklist_name')
        # Filters for any matches of this string with any in the database
        existing_checklist = Checklist.query.filter_by(checklist_name=new_checklist_name).first()
        # If Truthy, the message is flashed
        if existing_checklist:
            flash("Checklist name already taken")
            return redirect(url_for('add_checklist_item'))
        # If Falsy, the item is committed to the database
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
        new_checklist_name = request.form.get('checklist_name')
        # Gets the string from in the checklist name box
        existing_checklist = Checklist.query.filter_by(checklist_name=new_checklist_name).first()
        # Filters for any matches of this string with any in the database
        if existing_checklist:
            # If Truthy, the message is flashed
            if existing_checklist.id != checklist_item_id:
                # Checks if the ID is the same, so the name can stay the same
                flash("Checklist name already taken")
                return redirect(url_for('edit_checklist_item', checklist_item_id=checklist_item_id))
                # if it's a different ID, the Checklist name taken message is flashed
            else:
                # If not, the change is committed to the database
                checklist_item.checklist_name=request.form.get("checklist_name"),
                checklist_item.checklist_notes=request.form.get("checklist_notes"),    
                checklist_item.checklist_date=request.form.get("checklist_date"),
                checklist_item.checklist_payment=bool(True if request.form.get("checklist_payment") else False)
                db.session.commit()
                return redirect(url_for("checklist"))
        else:
            # If not, the change is committed to the database
            checklist_item.checklist_name=request.form.get("checklist_name"),
            checklist_item.checklist_notes=request.form.get("checklist_notes"),    
            checklist_item.checklist_date=request.form.get("checklist_date"),
            checklist_item.checklist_payment=bool(True if request.form.get("checklist_payment") else False)
            db.session.commit()
            return redirect(url_for("checklist"))
    return render_template("edit_checklist_item.html", checklist_item=checklist_item)

@app.route("/delete_checklist_item/<int:checklist_item_id>")
def delete_checklist_item(checklist_item_id):
    checklist_item = Checklist.query.get_or_404(checklist_item_id)
    db.session.delete(checklist_item)
    db.session.commit()
    return redirect(url_for("checklist"))

# Guest Pages
@app.route("/guests")
def guests():
    guests = list(Guest.query.order_by(Guest.guest_name).all())
    return render_template("guests.html", guests=guests)

@app.route("/add_guests", methods=["GET", "POST"])
def add_guests():
    tables = list(Table.query.order_by(Table.table_name).all())
    if request.method == "POST":
        guest = Guest(
            guest_name=request.form.get("guest_name"),
            guest_notes=request.form.get("guest_notes"),
            table_number=request.form.get("table_number")
        )
        db.session.add(guest)
        db.session.commit()
        return redirect(url_for("guests"))
    return render_template("add_guests.html", tables=tables)

@app.route("/edit_guests/<int:guest_id>", methods=["GET", "POST"])
def edit_guests(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    tables = list(Table.query.order_by(Table.table_name).all())
    if request.method == "POST":
        guest.guest_name=request.form.get("guest_name"),
        guest.guest_notes=request.form.get("guest_notes"),    
        guest.table_number=request.form.get("table_number")
        db.session.commit()
        return redirect(url_for("guests"))
    return render_template("edit_guests.html", guest=guest, tables=tables)

@app.route("/delete_guest/<int:guest_id>")
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    db.session.delete(guest)
    db.session.commit()
    return redirect(url_for("guests"))


# Table Plan Pages
@app.route("/table_plan")
def table_plan():
    tables = list(Table.query.order_by(Table.table_name).all())
    return render_template("table_plan.html", tables=tables)

@app.route("/add_table", methods=["GET", "POST"])
def add_table():
    if request.method == "POST":
        table = Table(
            table_name=request.form.get("table_name"),
        )
        db.session.add(table)
        db.session.commit()
        return redirect(url_for("table_plan"))
    return render_template("add_table.html")

@app.route("/edit_table/<int:table_id>", methods=["GET", "POST"])
def edit_table(table_id):
    table = Table.query.get_or_404(table_id)
    if request.method == "POST":
        table.table_name=request.form.get("table_name"),
        db.session.commit()
        return redirect(url_for("table_plan"))
    return render_template("edit_table.html", table=table)

@app.route("/delete_table/<int:table_id>")
def delete_table(table_id):
    table = Table.query.get_or_404(table_id)
    db.session.delete(table)
    db.session.commit()
    return redirect(url_for("table_plan"))

# Payments Pages
@app.route("/payments")
def payments():
    checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
    return render_template("payments.html", checklist_items=checklist_items)