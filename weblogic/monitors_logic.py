from webdata import monitors_data


def get_monitors():
	payload = monitors_data.list_monitors()
	return payload


def post_monitor(guid):
	pass


def get_monitor(guid):
	pass


def post_monitor_create(json_body):
	payload = monitors_data.create_monitor(json_body)
	return payload


def delete_monitor(guid):
	pass
