from flask import Flask
import os

template_dir = os.path.abspath('ui/templates')
print(template_dir)
app = Flask(__name__, static_folder=os.path.abspath('static'), template_folder=os.path.abspath('templates'))

from . import monitors_api
from . import videos_api
from . import users_api
from . import schedule_api
