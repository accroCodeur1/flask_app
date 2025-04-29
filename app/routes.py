from flask import Blueprint, jsonify, render_template
import os
import yaml
import json

bp = Blueprint('main', __name__)

def load_data(file_name):
    data_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        with open(data_path, 'r') as file:
            return yaml.safe_load(file)
    elif file_name.endswith('.json'):
        with open(data_path, 'r') as file:
            return json.load(file)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/api/events')
def get_events():
    events = load_data('events.json')
    return jsonify(events)

@bp.route('/api/news')
def get_news():
    news = load_data('news.json')
    return jsonify(news)