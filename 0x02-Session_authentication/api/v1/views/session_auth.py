#!/usr/bin/env python3
""" Route handles
"""
from werkzeug import exceptions
from api.v1.views import app_views
from flask import jsonify, request, abort
from os import getenv
from models.user import User


@app_views.route('auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/V1/auth/session/login
    """
    email = request.form.get('email')
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    cookie = getenv('SESSION_NAME')
    user_obj = jsonify(user.to_json())

    user_obj.set_cookie(cookie, session_id)
    return user_obj


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth/session/logout
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
