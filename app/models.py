from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship


# class ProductType(Model):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True, nullable=False)
#
#     def __repr__(self):
#         return self.name


class Person(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    birthday = Column(Integer)

    def __repr__(self):
        return self.name


class Client(User):
    __tablename__ = "ab_user"
    extra = Column(String(50), unique=True, nullable=False)
