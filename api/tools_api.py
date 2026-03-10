from flask import Blueprint, request, jsonify
import random
import string

tools_api = Blueprint("tools_api",__name__)

@tools_api.route("/api/random-number")
def random_number():

    return jsonify({
        "number": random.randint(1,100)
    })


@tools_api.route("/api/password")
def password():

    length = int(request.args.get("length",12))

    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))

    return jsonify({"password":password})