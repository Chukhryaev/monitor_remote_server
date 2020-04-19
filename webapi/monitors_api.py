from flask import request
from weblogic import monitors
from webapi import *


@app.route('/monitors', methods=['GET'])
def get_monitors():
	return monitors.get_monitors()


@app.route('/monitor/<guid>', methods=['GET', 'POST', 'DELETE'])
def guid_monitor(guid):
	if request.method == "GET" and guid:
		return monitors.get_monitor(guid)
	if request.method == "POST" and guid:
		return monitors.post_monitor(guid)
	if request.method == "DELETE" and guid:
		return monitors.delete_monitor(guid)


@app.route('/monitor', methods=['POST'])
def post_monitor():
	return monitors.post_monitor_create(request.json)
