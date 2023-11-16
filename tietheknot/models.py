from tietheknot import db

class Checklist(db.Model):
    # Schema for the Checklist model
    id = db.Column(db.Integer, primary_key=True)
    checklist_name = db.Column(db.String(30), unique=True, nullable=False)
    checklist_notes = db.Column(db.Text)
    checklist_date = db.Column(db.Date, nullable=False)
    checklist_payment = db.Column(db.Boolean)

    
    def __repr__(self):
        # Represents itself as a string
        return self.checklist_name

class Table(db.Model):
    # Schema for the Payments model
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(30), unique=True, nullable=False)
    guest_rel = db.relationship("Guest", backref="table", cascade="all, delete", lazy=True)

    def __repr__(self):
        # Represents itself as a string
        return self.table_name

class Guest(db.Model):
    # Schema for the Guests model
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(30), nullable=False)
    guest_notes = db.Column(db.Text)
    table_number = db.Column(db.String(30), db.ForeignKey("table.table_name", ondelete="CASCADE"))

    def __repr__(self):
        # Represents itself as a string
        return self.guest_name