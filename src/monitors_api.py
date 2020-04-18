# from flask import request
from src import *


@app.route('/monitors')
def get_monitors():
	return dict({"monitors": [
		{
			'guid': 'guid123',
			'name': 'Dev monitor',
			'status': 'active'
		},
		{
			'guid': 'guid321312',
			'name': 'Stage monitor',
			'status': 'Dead'
		}]})
