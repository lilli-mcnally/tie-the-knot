from tietheknot import db

class User(db.Model):
    # Schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name_one = db.Column(db.String(15), nullable=False)
    name_two = db.Column(db.String(15), nullable=False)
    wedding_date = db.Column(db.Date, nullable=False)
    checklist_rel = db.relationship("Checklist", backref="user", lazy=True)
    guest_rel = db.relationship("Guest", backref="user", lazy=True)
    table_rel = db.relationship("Table", backref="user", lazy=True)

    def __repr__(self):
        #Represents itself as a string
        return self.username

class Checklist(db.Model):
    # Schema for the Checklist model
    id = db.Column(db.Integer, primary_key=True)
    checklist_name = db.Column(db.String(30), unique=True, nullable=False)
    checklist_notes = db.Column(db.Text)
    checklist_date = db.Column(db.Date, nullable=False)
    checklist_payment = db.Column(db.Boolean)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self):
        # Represents itself as a string
        return self.checklist_name

class Guest(db.Model):
    # Schema for the Guests model
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(30), nullable=False)
    guest_notes = db.Column(db.Text)
    table_number = db.Column(db.Integer, db.ForeignKey("table.id"))
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        # Represents itself as a string
        return self.guest_name

class Table(db.Model):
    # Schema for the Payments model
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(30), unique=True, nullable=True)
    guests = db.relationship("Guest", backref="table", lazy=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        # Represents itself as a string
        return self.table_name