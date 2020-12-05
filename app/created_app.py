from flask import Flask
from flask import jsonify

def created_app():
    app = Flask(__name__)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app