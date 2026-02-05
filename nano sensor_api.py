  GNU nano 8.4              sensor_api.py
# sensor_api.py
from flask import Blueprint, request, jsonify, current_app
from decorators import check_replay
from flask_jwt_extended import jwt_required, verify_jwt_in_requ>
import json, os
from pathlib import Path

bp = Blueprint("sensor", __name__, url_prefix="/sensor")
DATA_FILE = Path(__file__).parent / "sensor_ingest.jsonl"

def append_line(obj):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

@bp.route("/ingest", methods=["POST"])
def ingest():
    """
    Expected payload:
     {"nonce":"unique-id","time": epoch, "vbus":..., "accel":{.>
    Headers: either JWT auth or a pre-shared header X-PSK (for >
    """
    js = request.get_json(force=True)
    nonce = js.get("nonce")
    ts = js.get("time")
    # replay protection
    if not nonce or not ts:
        return jsonify({"msg":"nonce and time required"}), 400
                       [ Read 59 lines ]
^G Help     ^O Write Out^F Where Is ^K Cut      ^T Execute
^X Exit     ^R Read File^\ Replace  ^U Paste    ^J Justify
