import logging
from mysql import connector

log = logging.getLogger(__name__)


class ClassDBConnection:
	def __init__(self, host, port, username, password, database):
		self.host = host
		self.port = port
		self.username = username
		self.password = password
		self.database = database
		self.connection = None
		self.cursor = None

	def connect(self):
		if self.connection is None:
			log.debug("Connecting to DB")
			self.connection = connector.connect(
				host=self.host,
				port=self.port,
				user=self.username,
				passwd=self.password,
				database=self.database
			)
			self.cursor = self.connection.cursor()

	def execute(self, sql, value):
		if self.connection is None:
			self.connect()
		self.cursor.execute(sql, value)
		self.connection.commit()
		return self.cursor

	def executemany(self, sql, values):
		if self.connection is None:
			self.connect()
		self.cursor.executemany(sql, values)
		self.connection.commit()
		return self.cursor

	def fetchall(self, sql, val=None):
		if self.connection is None:
			self.connect()
		self.cursor.execute(sql, val)
		return self.cursor.fetchall()

	def fetchone(self, sql, val=None):
		if self.connection is None:
			self.connect()
		self.cursor.execute(sql, val)
		return self.cursor.fetchone()

	def close(self):
		if self.connection is not None:
			log.debug("Disconnect from DB")
			self.cursor.close()
			self.connection.close()
