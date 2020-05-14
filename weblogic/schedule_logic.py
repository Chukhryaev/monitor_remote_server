from webdata import schedule_data
import hashlib
import config


def _default_json():
	return {
		"step": config.step,
		"videos": []
	}


def get_schedules():
	pass


def get_schedule(guid):
	pass


def post_schedule(guid, request_json):
	pass


def get_monitor_schedule_by_date(monitor_guid, date):
	try:
		guid = hashlib.md5(f"{monitor_guid}{date}".encode()).hexdigest().upper()
		payload = schedule_data.get_schedule(guid)
		if not payload:
			payload = _create_monitor_schedule_by_date(guid, monitor_guid, date, _default_json())
			if payload.get("code") == "error":
				return payload
			payload = schedule_data.get_schedule(guid)
			return payload
		return payload
	except Exception as e:
		return dict({"code": "error", "error": e})


def update_monitor_schedule_by_date(monitor_guid, date, json_body):
	pass


def _create_monitor_schedule_by_date(guid, monitor_guid, date, json_body=None):

	return dict()
