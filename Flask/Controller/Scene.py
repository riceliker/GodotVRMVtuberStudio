from flask import Blueprint, send_from_directory
import os

bp = Blueprint("Scene", __name__)

GODOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../Web/Godot")
)

@bp.route("/")
def Scene():
    print(os.path.dirname(__file__))
    return send_from_directory(GODOT_DIR, "Godot.html")

@bp.route("/<path:filename>")
def godot_static(filename):
    return send_from_directory(GODOT_DIR, filename)