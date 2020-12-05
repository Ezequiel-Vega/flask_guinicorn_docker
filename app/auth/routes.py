from . import auth_bp as app
from flask import jsonify

@app.route('/auth')
def auth():
    return jsonify({'msg': 'Authentication'}), 200