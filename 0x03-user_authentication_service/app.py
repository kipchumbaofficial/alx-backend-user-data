#!/usr/bin/env python3
""" Flask app
"""
from flask import (
        Flask,
        jsonify,
        request,
        abort
        redirect)
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    """ The page of the flask app
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ Registers users
    """
    email = request.form['email']
    password = request.form['password']

    try:
        AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"})
    except ValueError:
        return jsonify({
            "message": "email already registered"
            }), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ Login user by creating a session Id cookie
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)
    is_loggedin = AUTH.valid_login(
            request.form['email'],
            request.form['password']
            )
    if is_loggedin:
        session_id = AUTH.create_session(email)
        response = jsonify({
            "email": email,
            "message": "logged in"
            })
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Logs out a user
    """
    session_id = request.cookies.get("session_id", None)
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect(url_for('app.users'))
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
