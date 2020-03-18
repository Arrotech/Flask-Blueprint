from flask import render_template
from app.api.v1 import blueprint1

# blueprint1 = Blueprint('blueprint1', __name__, template_folder='../../../../templates', static_folder='../../../../static')


@blueprint1.route('/home')
def index():
    return render_template('orders.html')
