from flask import Flask
from app.api.v1.views.orders import blueprint1



app = Flask(__name__)
app.register_blueprint(blueprint1, url_prefix='/app/')
