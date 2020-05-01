from webdata import monitors_data


def get_monitors():
	try:
		payload = monitors_data.list_monitors()
		return payload
	except Exception as e:
		return dict({"code": "error", "error": e})


def post_monitor(guid, json_body):
	try:
		payload = monitors_data.update_monitor(guid, json_body)
		if payload.rowcount == 1:
			payload = get_monitors()
			return payload
		return dict({"code": "error", "error": f"Something happened while updating monitor {guid}"})
	except IndexError as e:
		return dict({"code": "error", "error": e})
	except Exception as e:
		return dict({"code": "error", "error": e})


def get_monitor(guid):
	try:
		payload = monitors_data.get_monitor(guid)
		return payload
	except Exception as e:
		return dict({"code": "error", "error": e})


def post_monitor_create(json_body):
	try:
		payload = monitors_data.create_monitor(json_body)
		if payload.rowcount == 1:
			payload = get_monitors()
			return payload
		return dict({"code": "error", "error": "Something happened while creating new monitor"})
	except IndexError as e:
		return dict({"code": "error", "error": e})
	except Exception as e:
		return dict({"code": "error", "error": e})


def delete_monitor(guid):
	try:
		payload = monitors_data.delete_monitor(guid)
		if payload.rowcount == 1:
			payload = get_monitors()
			return payload
		return dict({"code": "error", "error": f"Something happened while deleting monitor {guid}"})
	except IndexError as e:
		return dict({"code": "error", "error": e})
	except Exception as e:
		return dict({"code": "error", "error": e})
