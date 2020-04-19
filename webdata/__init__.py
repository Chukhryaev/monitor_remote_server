import config
from common.ClassDBConnection import ClassDBConnection


database_instance = ClassDBConnection(
	host=config.db_setting.get("host"),
	port=config.db_setting.get("port"),
	username=config.db_setting.get("user"),
	password=config.db_setting.get("password"),
	database=config.db_setting.get("database")
)

from . import monitors_data
