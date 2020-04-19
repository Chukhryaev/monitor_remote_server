from flask import request
from weblogic import users
from webapi import *


@app.route("/users", methods=["GET"])
def get_users():
	return users.get_users()


@app.route("/user/<guid>", methods=["GET", "POST"])
def guid_user(guid):
	if request.method == "GET":
		return users.get_user(guid)
	if request.method == "POST":
		return users.post_user(guid)


@app.route("/user", methods=["POST"])
def create_user():
	return users.create_user()
