from webdata import *
import hashlib
import datetime


def list_monitors():
    try:
        sql = "SELECT * from Monitors"
        monitors = database_instance.fetchall(sql)
        return dict(
            {"code": "get.list",
             "monitors": [{"guid": monitor[1], "name": monitor[2], "location": monitor[3]} for monitor in monitors]})
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
        if result.rowcount == 1:
            return list_monitors()
    except IndexError as e:
        return dict({"code": "error", "error": e})
    except Exception as e:
        return dict({"code": "error", "error": e})


if __name__ == "__main__":
    body = {
        "monitor": {
            "name": "Monitor_dev_test",
            "location": f"EUROPA{str(datetime.datetime.today())}"
        }
    }
    print(create_monitor(body))
    print(list_monitors())
