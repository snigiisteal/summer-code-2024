from website._init_ import db
from sqlalchemy import func

class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(40),unique=True,nullable=False)
    name=db.Column(db.String(40),unique=True,nullable=False)
    phone_number=db.Column(db.Integer,unique=True)
    gender=db.Column(db.String(10),unique=True)
    activities = db.relationship('Activity')


class Activity(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    steps = db.Column(db.Integer)
    move_mins=db.Column(db.Integer)
    energy_expended=db.Column(db.Integer)
    kilometers=db.Column(db.Integer)
    person_id=db.Column(db.Integer,db.ForeignKey('person.id'))


def insert_into_database(id,email,name,steps,move_mins):
    print("database")
    person = Person(id=id,email=email,name=name)
    db.session.add(person)   
    db.session.commit()
    act = Activity(steps=steps,move_mins=move_mins)
    db.session.add(act)   
    db.session.commit()
    
