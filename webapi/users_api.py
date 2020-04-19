from flask import request
from weblogic import users_logic
from webapi import *


@app.route("/users", methods=["GET"])
def get_users():
	return users_logic.get_users()


@app.route("/user/<guid>", methods=["GET", "POST"])
def guid_user(guid):
	if request.method == "GET":
		return users_logic.get_user(guid)
	if request.method == "POST":
		return users_logic.post_user(guid)


@app.route("/user", methods=["POST"])
def create_user():
	return users_logic.create_user()
