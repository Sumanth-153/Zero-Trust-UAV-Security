  GNU nano 8.4              flight_api.py
# flight_api.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from decorators import role_required

bp = Blueprint("flight", __name__, url_prefix="/flight")

@bp.route("/command", methods=["POST"])
@role_required("operator")   # operator or admin allowed
def send_command():
    """
    Example: {"cmd":"land","params":{...}}
    In real system: commands would be signed + queued to flight>
    """
    js = request.get_json(force=True)
    cmd = js.get("cmd")
    if not cmd:
        return jsonify({"msg":"cmd required"}), 400
    # For demo: simply ack and emit to SocketIO if present
    from flask import current_app
    sio = current_app.extensions.get("socketio")
    if sio:
        sio.emit("command", {"cmd":cmd, "params":js.get("params>
    return jsonify({"msg":"sent","cmd":cmd})




                       [ Read 24 lines ]
^G Help     ^O Write Out^F Where Is ^K Cut      ^T Execute
^X Exit     ^R Read File^\ Replace  ^U Paste    ^J Justify
