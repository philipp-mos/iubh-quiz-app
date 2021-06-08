from flask import Blueprint
from flask import render_template
from flask_login import login_required

subjects_controller = Blueprint(
    'subjects_controller',
    __name__,
    template_folder='views',
    url_prefix='/subjects'
)


@subjects_controller.before_request
@login_required
def before_request():
    pass



## Subjects/Overview ##
@subjects_controller.route('/overview', methods=['GET'])
def subjects():
    """
    Subjects Overview
    """

    return render_template('overview.jinja2')
