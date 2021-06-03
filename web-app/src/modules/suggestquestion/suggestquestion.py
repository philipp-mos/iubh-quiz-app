from flask import Blueprint
from flask import render_template
from flask_login import login_required


suggestquestion_controller = Blueprint(
    'suggestquestion_controller',
    __name__,
    template_folder='views',
    url_prefix='/suggest-question'
)


@suggestquestion_controller.before_request
@login_required
def before_request():
    pass



## SuggestQuestion/Index ##
@suggestquestion_controller.route('/', methods=['GET'])
def index():
    """
    Question-Suggest First Page
    """

    return render_template('suggestquestion_index.jinja2')
