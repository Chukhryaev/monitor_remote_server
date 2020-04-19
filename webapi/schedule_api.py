from flask import request
from weblogic import schedule_logic
from webapi import *


@app.route("/schedules", methods=["GET"])
def get_schedules():
	return schedule_logic.get_schedules()


@app.route("/schedule/<guid>", methods=["GET", "POST"])
def guid_schedules(guid):
	if request.method == "GET":
		return schedule_logic.get_schedule(guid)
	if request.method == "POST":
		return schedule_logic.post_schedule(guid)


@app.route("/schedule/<date>", methods=["POST"])
def create_schedule(date):
	return schedule_logic.create_schedule(date)
