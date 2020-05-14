from webdata import *
import hashlib
import datetime


def list_schedules():
	pass


def get_schedule(guid):
	try:
		sql = "SELECT GUID, body, date FROM Schedule WHERE GUID = %s"
		val = [guid]
		result = database_instance.fetchone(sql, val)
		return result
	except Exception as e:
		return dict({"code": "error", "error": e})


def update_schedule(guid, monitor_guid, json_body):
	pass


def create_schedule(guid, monitor_guid, json_body=None):
	pass
