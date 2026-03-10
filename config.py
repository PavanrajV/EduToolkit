import os

class Config:
    SECRET_KEY = "edutoolkit_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///edutoolkit.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False