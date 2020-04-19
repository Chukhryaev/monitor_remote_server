import hashlib
import time
from weblogic import *


def get_monitors():
	sql = "SELECT * from Monitors"
	return dict({"monitors": database_instance.fetchall(sql)})


def post_monitor(guid):
	pass


def get_monitor(guid):
	pass


def post_monitor_create(json_body):
	try:
		name = json_body.monitor.name
		location = json_body.monitor.location
		hash_instance = hashlib.blake2s(digest_size=32)
		hash_instance.update(location)
		hash_instance.update(name)
		guid = hash_instance.hexdigest()
		sql = "INSERT INTO Monitors (SKEY, GUID, name, location) VALUES (%s, %s, %s, %s)"
		val = (None, guid, name, location)
		result = database_instance.execute(sql, val)
		if result.rowcount == 1:
			return get_monitors()
	except IndexError as e:
		return dict({"code": "error", "error": e})
	except Exception as e:
		return dict({"code": "error", "error": e})


def delete_monitor(guid):
	pass
