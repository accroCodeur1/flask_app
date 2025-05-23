from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Configuration de base
    app.config.from_pyfile('config.py')
    
    # Enregistrement des blueprints
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app