from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma=Marshmallow()
db=SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(250), nullable=False)
    email=db.Column(db.String(250), nullable=True)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=User