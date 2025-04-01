from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
import logging
from routes import bp as api_bp

app = Flask(__name__)
CORS(app)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300})

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_app():
    app.register_blueprint(api_bp)
    return app

if __name__ == "__main__":
    create_app().run(debug=True)