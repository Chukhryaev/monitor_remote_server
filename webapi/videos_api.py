from flask import request
from weblogic import videos
from webapi import *


@app.route("/videos", methods=["GET"])
def get_videos():
	return videos.get_videos()


@app.route("/video/<guid>", methods=["GET", "POST"])
def guid_videos(guid):
	if request.method == "GET":
		return videos.get_video(guid)
	if request.method == "POST":
		return videos.post_video(guid)


@app.route("/video", methods=["POST"])
def add_video():
	return videos.add_video()
