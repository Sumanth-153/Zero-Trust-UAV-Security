  GNU nano 8.4              admin_api.py
# admin_api.py
from flask import Blueprint, jsonify, request
from decorators import role_required
from auth_api import _load_users, _save_users
bp = Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/users", methods=["GET"])
@role_required("admin")
def list_users():
    users = _load_users()
    # hide secrets
    out = {u: {"role": users[u].get("role"), "created": users[u>
    return jsonify(out)

@bp.route("/users/<username>", methods=["DELETE"])
@role_required("admin")
def del_user(username):
    users = _load_users()
    if username not in users:
        return jsonify({"msg":"not found"}), 404
    del users[username]
    _save_users(users)
    return jsonify({"msg":"deleted"})





                       [ Read 23 lines ]
^G Help     ^O Write Out^F Where Is ^K Cut      ^T Execute
^X Exit     ^R Read File^\ Replace  ^U Paste    ^J Justify
