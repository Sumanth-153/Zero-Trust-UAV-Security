  GNU nano 8.4               auth_api.py
# auth_api.py
import os, json, time, secrets
from pathlib import Path
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_pas>
from flask_jwt_extended import create_access_token, get_jwt, jw>
import pyotp

USERS_FILE = Path(__file__).parent / "users.json"
bp = Blueprint("auth", __name__, url_prefix="/auth")

def _load_users():
    if not USERS_FILE.exists():
        return {}
    return json.loads(USERS_FILE.read_text())

def _save_users(u):
    USERS_FILE.write_text(json.dumps(u, indent=2))

def create_user(username, password, role="operator"):
    users = _load_users()
    if username in users:
        raise ValueError("user exists")
    otp_secret = pyotp.random_base32()
    users[username] = {
        "pw_hash": generate_password_hash(password),
        "role": role,
        "otp_secret": otp_secret,
                       [ Read 88 lines ]
^G Help     ^O Write Out^F Where Is ^K Cut      ^T Execute
^X Exit     ^R Read File^\ Replace  ^U Paste    ^J Justify
