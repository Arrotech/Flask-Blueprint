from flask import Flask
from app.api.v1 import blueprint1 as api_blueprint1



app = Flask(__name__)
app.register_blueprint(api_blueprint1, url_prefix='/app')
