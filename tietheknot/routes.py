from flask import render_template, request, redirect, url_for, flash, session
from tietheknot import app, db
from tietheknot.models import User, Checklist, Table, Guest
from werkzeug.security import generate_password_hash, check_password_hash

# Home Page
@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for('dashboard'))
    return render_template("home.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if "user" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        new_username = request.form.get("username")
        existing_user = User.query.filter_by(username=new_username).first()
        if existing_user:
            flash("Username is already taken")
            return redirect(url_for('sign_up'))

        new_password = request.form.get("password")
        conf_password = request.form.get("conf_password")
        if new_password != conf_password:
            flash("Whoops! It looks like your passwords don't match")
            return redirect(url_for('sign_up'))

        sign_up = User(
            username=request.form.get("username"),
            password=generate_password_hash(request.form.get("password")),
            name_one=request.form.get("name_one"),
            name_two=request.form.get("name_two"),
            wedding_date=request.form.get("wedding_date"),
        )
        db.session.add(sign_up)
        db.session.commit()
        session["user"] = request.form.get("username")
        flash("Sucessfully Signed Up!")
        return redirect(url_for('dashboard', username=session["user"]))
    return render_template("sign_up.html")

@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if "user" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username_input = request.form.get("username")
        existing_user = User.query.filter_by(username=username_input).first()
        if existing_user:
            if check_password_hash(
                existing_user.password, request.form.get("password")):
                session["user"] = request.form.get("username")
                return redirect(url_for('dashboard', username=session["user"]))
            else:
                flash("Username or Password was incorrect")
                return render_template("log_in.html")
        else:
            flash("Username or Password was incorrect")
            return render_template("log_in.html")
    return render_template("log_in.html")

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user")
        flash("Successfully logged out")
        return redirect(url_for("log_in"))
    return redirect(url_for("log_in"))


# If user is logged in
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        return render_template("edit_profile.html", username=username)
    return redirect(url_for("log_in"))

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
        return render_template("dashboard.html", checklist_items=checklist_items, username=username)
    return redirect(url_for("log_in"))


# Checklist Pages
@app.route("/checklist")
def checklist():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        print(session["user"])
        print(username)
        all_checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
        checklist_items = Checklist.query.filter_by(created_by=session["user"]).all()
        return render_template("checklist.html", checklist_items=checklist_items, username=username)
    return redirect(url_for("log_in"))


@app.route("/add_checklist_item", methods=["GET", "POST"])
def add_checklist_item():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
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
                checklist_payment=bool(True if request.form.get("checklist_payment") else False),
                created_by = session["user"]
            )
            db.session.add(checklist_item)
            db.session.commit()
            return redirect(url_for("checklist"))
        return render_template("add_checklist_item.html", username=username)
    return redirect(url_for("log_in"))

@app.route("/edit_checklist_item/<int:checklist_item_id>", methods=["GET", "POST"])
def edit_checklist_item(checklist_item_id):
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        checklist_item = Checklist.query.get_or_404(checklist_item_id)
        if username == checklist_item.created_by:
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
            return render_template("edit_checklist_item.html", checklist_item=checklist_item, username=username)
        return redirect(url_for("log_in"))
    return redirect(url_for("log_in"))

@app.route("/delete_checklist_item/<int:checklist_item_id>")
def delete_checklist_item(checklist_item_id):
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        checklist_item = Checklist.query.get_or_404(checklist_item_id)
        db.session.delete(checklist_item)
        db.session.commit()
        return redirect(url_for("checklist"))
    return redirect(url_for("log_in"))

# Guest Pages
@app.route("/guests")
def guests():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        guests = list(Guest.query.order_by(Guest.guest_name).all())
        return render_template("guests.html", guests=guests, username=username)
    return redirect(url_for("log_in"))

@app.route("/add_guests", methods=["GET", "POST"])
def add_guests():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        tables = list(Table.query.order_by(Table.table_name).all())
        if request.method == "POST":
            guest = Guest(
                guest_name=request.form.get("guest_name"),
                guest_notes=request.form.get("guest_notes"),
                created_by = session["user"]
            )
            if request.form.get("table_name") != 'None':
                guest.table_number=Table.query.filter_by(table_name=request.form.get("table_name")).first().id
            else:
                guest.table_number=0
            db.session.add(guest)
            db.session.commit()
            return redirect(url_for("guests"))
        return render_template("add_guests.html", tables=tables, username=username)
    return redirect(url_for("log_in"))

@app.route("/edit_guests/<int:guest_id>", methods=["GET", "POST"])
def edit_guests(guest_id):
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        guest = Guest.query.get_or_404(guest_id)
        tables = list(Table.query.order_by(Table.table_name).all())
        if request.method == "POST":
            guest.guest_name=request.form.get("guest_name"),
            guest.guest_notes=request.form.get("guest_notes"),
            if request.form.get("table_name") != 'None':
                guest.table_number=Table.query.filter_by(table_name=request.form.get("table_name")).first().id
            else:
                guest.table_number=0
            db.session.commit()
            return redirect(url_for("guests"))
        return render_template("edit_guests.html", guest=guest, tables=tables, username=username)
    return redirect(url_for("log_in"))

@app.route("/delete_guest/<int:guest_id>")
def delete_guest(guest_id):
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        guest = Guest.query.get_or_404(guest_id)
        db.session.delete(guest)
        db.session.commit()
        return redirect(url_for("guests"), username=username)
    return redirect(url_for("log_in"))

# Table Plan Pages
@app.route("/table_plan")
def table_plan():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        tables = list(Table.query.order_by(Table.id).all())
        guests = list(Guest.query.order_by(Guest.guest_name).all())
        return render_template("table_plan.html", tables=tables, guests=guests, username=username)
    return redirect(url_for("log_in"))

@app.route("/add_table", methods=["GET", "POST"])
def add_table():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        if request.method == "POST":
            # Gets the string from in the table name box
            new_table_name = request.form.get('new_table')
            # Filters for any matches of this string with any in the database
            existing_table = Table.query.filter_by(table_name=new_table_name).first()
            # If Truthy, the message is flashed
            if existing_table:
                flash("Table name already taken")
                return redirect(url_for('add_table'))
            # If Falsy, the table is committed to the database
            table = Table(
                table_name=request.form.get("new_table"),
                created_by = session["user"]
            )
            db.session.add(table)
            db.session.commit()
            return redirect(url_for("table_plan"))
        return render_template("add_table.html", username=username)
    return redirect(url_for("log_in"))

@app.route("/edit_table/<int:table_id>", methods=["GET", "POST"])
def edit_table(table_id):
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        table = Table.query.get_or_404(table_id)
        if request.method == "POST":
            table.table_name=request.form.get("new_table"),
            db.session.commit()
            return redirect(url_for("table_plan"))
        return render_template("edit_table.html", table=table, username=username)
    return redirect(url_for("log_in"))

@app.route("/delete_table/<int:table_id>")
def delete_table(table_id):
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        table = Table.query.get_or_404(table_id)
        db.session.delete(table)
        db.session.commit()
        return redirect(url_for("table_plan"), username=username)
    return redirect(url_for("log_in"))

# Payments Pages
@app.route("/payments")
def payments():
    if "user" in session:
        username = User.query.filter_by(username=session["user"]).first()
        checklist_items = list(Checklist.query.order_by(Checklist.checklist_date).all())
        return render_template("payments.html", checklist_items=checklist_items, username=username)
    return redirect(url_for("log_in"))