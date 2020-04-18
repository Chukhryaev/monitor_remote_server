from flask import Flask
import os

app = Flask(__name__, static_folder=os.path.abspath('../../ui'))

from . import monitors_api
