from flask import Blueprint
from flask import render_template


home_controller = Blueprint(
    'home_controller',
    __name__,
    template_folder='views',
    url_prefix=''
)


## Home/Index ##
@home_controller.route('/', methods=['GET'])
def index():
    return render_template('index.jinja2')
