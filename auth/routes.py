from flask import Blueprint, request, jsonify
from database.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():

    data = request.json

    user = User(
        username=data["username"],
        email=data["email"],
        password=generate_password_hash(data["password"])
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message":"User registered"})
    

@auth.route("/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(email=data["email"]).first()

    if user and check_password_hash(user.password,data["password"]):
        return jsonify({"message":"Login success"})
    
    return jsonify({"message":"Invalid login"})