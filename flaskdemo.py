#!/usr/bin/python
from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route("/")
def authpassdemo():
    userName = request.headers.get('username')
    userGroups = request.headers.get('usergroups')
    if userName is None:
	userName = "Not logged in."
	userGroups = "Not logged in."
    content = ["Hello world", "Username: " + userName, "Groups: " + userGroups]
    return "<html>" + "<br>".join(content) + "</html>"

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080,threaded=False)
