from flask import Blueprint, jsonify

main = Blueprint("main",__name__)


@main.get("/")
def hello():
    return jsonify(message="Hello World"),200

@main.get("/health")
def health():
    return jsonify(status="ok",service="app api"),200

