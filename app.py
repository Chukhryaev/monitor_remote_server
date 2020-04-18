import config
from webapi import *

app.run(host=config.flask_setting.get("host"), port=config.flask_setting.get("port"))
