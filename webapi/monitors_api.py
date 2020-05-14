from flask import request
from flask import render_template
from weblogic import monitors_logic
from webapi import *


@app.route('/monitors', methods=['GET'])
def get_monitors():
	data = monitors_logic.get_monitors()
	# return data
	return render_template('monitors.html', data=data)


@app.route('/monitor/<guid>', methods=['GET', 'POST', 'DELETE'])
def guid_monitor(guid):
	if request.method == "GET" and guid:
		data = monitors_logic.get_monitor(guid)
		return render_template('monitor.html', data=data)
	if request.method == "POST" and guid:
		return monitors_logic.post_monitor(guid, request.json)
	if request.method == "DELETE" and guid:
		return monitors_logic.delete_monitor(guid)


@app.route('/monitor', methods=['POST'])
def post_monitor():
	return monitors_logic.post_monitor_create(request.json)
