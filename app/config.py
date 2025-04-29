import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'data')