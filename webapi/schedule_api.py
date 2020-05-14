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
		return schedule_logic.post_schedule(guid, request.json)


@app.route("/monitor/<guid>/schedule/<date>", methods=["GET", "POST"])
def monitor_date_schedule(guid, date):
	if request.method == "GET":
		return schedule_logic.get_monitor_schedule_by_date(guid, date)
	if request.method == "POST":
		return schedule_logic.update_monitor_schedule_by_date(guid, date, request.json)
