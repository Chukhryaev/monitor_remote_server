from flask import request
from weblogic import videos_logic
from webapi import *


@app.route("/videos", methods=["GET"])
def get_videos():
	return videos_logic.get_videos()


@app.route("/video/<guid>", methods=["GET", "POST"])
def guid_videos(guid):
	if request.method == "GET":
		return videos_logic.get_video(guid)
	if request.method == "POST":
		return videos_logic.post_video(guid)


@app.route("/video", methods=["POST"])
def add_video():
	return videos_logic.add_video()
