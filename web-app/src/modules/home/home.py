from flask import Blueprint
from flask import render_template
from flask_login import login_required


home_controller = Blueprint(
    'home_controller',
    __name__,
    template_folder='views',
    url_prefix=''
)


## Home/Index ##
@home_controller.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.jinja2')
