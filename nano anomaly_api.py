  GNU nano 8.4             anomaly_api.py
# anomaly_api.py
import joblib
import numpy as np
from flask import Blueprint, request, jsonify

bp = Blueprint('anomaly_api', __name__, url_prefix='/anomaly')
_model = None

def load_model(path='models/anomaly_model.pkl'):
    global _model
    if _model is None:
        _model = joblib.load(path)
    return _model

@bp.route('/predict', methods=['POST'])
def predict():
    js = request.get_json(force=True)

    # vector for model (same order as training)
    vec = [
        js.get('accel_x', js.get('accel', {}).get('x', 0)),
        js.get('accel_y', js.get('accel', {}).get('y', 0)),
        js.get('accel_z', js.get('accel', {}).get('z', 0)),
        js.get('gyro_x', js.get('gyro', {}).get('x', 0)),
        js.get('gyro_y', js.get('gyro', {}).get('y', 0)),
        js.get('gyro_z', js.get('gyro', {}).get('z', 0)),
        js.get('vbus', 0),
        js.get('current_mA', js.get('current', 0)),

^G Help     ^O Write Out^F Where Is ^K Cut      ^T Execute
^X Exit     ^R Read File^\ Replace  ^U Paste    ^J Justify
