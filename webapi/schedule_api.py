from flask import request
from weblogic import schedule
from webapi import *


@app.route("/schedules", methods=["GET"])
def get_schedules():
	return schedule.get_schedules()


@app.route("/schedule/<guid>", methods=["GET", "POST"])
def guid_schedules(guid):
	if request.method == "GET":
		return schedule.get_schedule(guid)
	if request.method == "POST":
		return schedule.post_schedule(guid)


@app.route("/schedule/<date>")
def create_schedule(date):
	return schedule.create_schedule(date)
