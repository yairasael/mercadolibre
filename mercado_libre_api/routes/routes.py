import flask
from flask import request, g, redirect, url_for, abort
from flask.json import jsonify
from flask_cors import CORS
from controllers.controller import Search
app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route("/", methods=['GET'])
def searchCost():
    res = Search.searchCost(request.args)
    return res
