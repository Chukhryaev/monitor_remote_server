from webdata import *
import hashlib
import datetime


def list_monitors():
    try:
        sql = "SELECT GUID, name, location from Monitors"
        monitors = database_instance.fetchall(sql)
        return dict(
            {"code": "get.monitors.list", "monitors": [{
                "guid": monitor[0],
                "name": monitor[1],
                "location": monitor[2]
            } for monitor in monitors]})
    except Exception as e:
        return dict({"code": "error", "error": e})


def update_monitor(guid, json_body):
    try:
        sql = "UPDATE Monitors SET name = %s, location = %s WHERE GUID = %s"
        val = (json_body.get("name"), json_body.get("location"), guid)
        result = database_instance.execute(sql, val)
        return result
    except Exception as e:
        return dict({"code": "error", "error": e})


def get_monitor(guid):
    try:
        sql = "SELECT GUID, name, location FROM Monitors WHERE GUID = %s"
        val = [guid]
        result = database_instance.fetchone(sql, val)
        return dict({"code": "get.monitor", "monitor": {
            "guid": result[0],
            "name": result[1],
            "location": result[2]
        }})
    except Exception as e:
        return dict({"code": "error", "error": e})


def create_monitor(json_body):
    try:
        monitor = json_body.get("monitor")
        name = monitor.get("name")
        location = monitor.get("location")
        hash_instance = hashlib.blake2s(digest_size=16)
        hash_instance.update(location.encode("utf-8"))
        hash_instance.update(name.encode("utf-8"))
        guid = hash_instance.hexdigest()
        sql = "INSERT INTO Monitors (SKEY, GUID, name, location) VALUES (%s, %s, %s, %s)"
        val = (None, guid, name, location)
        result = database_instance.execute(sql, val)
        return result
    except Exception as e:
        return dict({"code": "error", "error": e})


def delete_monitor(guid):
    try:
        sql = "DELETE FROM Monitors WHERE GUID = %s"
        val = [guid]
        result = database_instance.execute(sql, val)
        return result
    except Exception as e:
        return dict({"code": "error", "error": e})


if __name__ == "__main__":
    body = {
        "monitor": {
            "name": "Monitor_dev_test",
            "location": f"EUROPA{str(datetime.datetime.today())}"
        }
    }
    guid = "e58eea456388e3abf4429d3ad06094c4"
    update_body = {
        "name": "NOT TEST DEV MONITOR",
        "location": f"EUROPA{str(datetime.datetime.today())}"
    }
    print(create_monitor(body))
    print(get_monitor(guid))
    print(update_monitor(guid, update_body))
    print(get_monitor(guid))
    print(delete_monitor(guid))
    print(get_monitor(guid))
    print(list_monitors())
