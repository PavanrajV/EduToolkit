from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(200))

class ToolUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(80))
    user_id = db.Column(db.Integer)