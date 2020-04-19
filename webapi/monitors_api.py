from flask import request
from weblogic import monitors_logic
from webapi import *


@app.route('/monitors', methods=['GET'])
def get_monitors():
	return monitors_logic.get_monitors()


@app.route('/monitor/<guid>', methods=['GET', 'POST', 'DELETE'])
def guid_monitor(guid):
	if request.method == "GET" and guid:
		return monitors_logic.get_monitor(guid)
	if request.method == "POST" and guid:
		return monitors_logic.post_monitor(guid)
	if request.method == "DELETE" and guid:
		return monitors_logic.delete_monitor(guid)


@app.route('/monitor', methods=['POST'])
def post_monitor():
	return monitors_logic.post_monitor_create(request.json)
