import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/tienda'
    SQLALCHEMY_TRACK_MODIFICATIONS = False