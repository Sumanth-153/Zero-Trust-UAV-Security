# ~/uav-dashboard/app.py
from flask import Flask, render_template, jsonify, request, red>
from flask_socketio import SocketIO, emit
import time, json, os, threading
from datetime import timedelta
from functools import wraps
import logging

from werkzeug.security import check_password_hash

from anomaly_api import bp as anomaly_bp

# ===============================
# AUDIT LOG FILE (NEW)
# ===============================
AUDIT_LOG_FILE = os.path.expanduser("~/uav-dashboard/audit.log")

def write_audit_log(user, role, action, request):
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "role": role,
        "action": action,
        "ip": request.remote_addr
    }
    with open(AUDIT_LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
