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

class Payments(db.Model):
    # Schema for the Payments model

class Guests(db.Model):
    # Schema for the Guests model
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(30), nullable=False)
    guest_notes = db.Column(db.Text)
    # table_number = db./// SOME KIND OF TABLE NUMBER STRING OR INTEGER
