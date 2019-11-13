from models.base_model import BaseModel
from flask_login import UserMixin
import peewee as pw


class User(BaseModel, UserMixin):
    name = pw.CharField(unique=False)
    email = pw.CharField(unique=False)
    password = pw.CharField(unique=False)


# class Email(BaseModel):
#     email = pw.CharField(unique=False)
#     usermail = pw.ForeignKeyField(User, backref="usermail")


# class Password(BaseModel):
#     password = pw.CharField(unique=False)
#     userpass = pw.ForeignKeyField(User, backref="userpass")
