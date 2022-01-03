from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.update(
    JWT_SECRET_KEY="please_change_this",
)

jwt = JWTManager(app)

users = {
    "username": generate_password_hash("password"),
}


@app.route("/login", methods=["POST"])
def login_page():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users:
        if check_password_hash(users.get(username), password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200

    return "Wrong credentials", 400


@app.route("/")
@jwt_required
def protected():
    return jsonify(logged_in_as=get_jwt_identity()), 200


if __name__ == "__main__":
    app.run()
