from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET'])
def helloworld():
    return jsonify({"message": "Welcome to the authentication module!"})


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return jsonify({"error": "User already exists"}), 400
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        login_user(user)
        return jsonify({"message": "Successfully logged in!", "user_id": user.id})
    return jsonify({"Error": "Invalid credentials"}), 401


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"})


@auth.route('/profile')
@login_required
def profile():
    return jsonify({"id": current_user.id,
                    "username": current_user.username,
                    "email": current_user.email})
