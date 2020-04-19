import logging
import time
from weblogic import *

log = logging.getLogger(__name__)


def get_monitors():
	sql = "SELECT * from Monitors"
	return str(database_instance.fetchall(sql))


def post_monitor(guid):
	pass


def get_monitor(guid):
	pass


def post_monitor_create():
	sql = "INSERT INTO Monitors (SKEY, GUID) VALUES (%s, %s)"
	val = (None, str(time.mktime(time.localtime())))
	result = database_instance.execute(sql, val)
	return str(result)


def delete_monitor(guid):
	pass
