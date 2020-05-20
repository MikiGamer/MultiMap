#!/usr/bin/env python3
from flask import Flask, Response
import http
import re
import requests

app = Flask(__name__)

def server(address):
    return "{\"addresses\":[\"%s\"],\"info\":{\"max_clients\":256,\"max_players\":8,\"passworded\":true,\"game_type\":\"DM\",\"name\":\"unnamed server\",\"map\":{\"name\":\"dm1\",\"crc\":\"f2159e6e\",\"size\":5805},\"version\":\"0.6.4\",\"clients\":[{\"name\":\"Learath2\",\"clan\":\"\",\"country\":-1,\"score\":-1,\"team\":1},{\"name\":\"deen\",\"clan\":\"DDNet\",\"country\":276,\"score\":0,\"team\":0}]}}" % address

@app.route("/servers.json")
def modhelp():
    return Response("{\"servers\":[%s]}" % ", ".join(server("127.0.0.1:{}".format(port)) for port in range(8303, 8400)), mimetype="application/json")
