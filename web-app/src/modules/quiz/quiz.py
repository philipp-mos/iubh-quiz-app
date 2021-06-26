from flask import Blueprint, render_template
from flask_login import login_required


quiz_controller = Blueprint(
    'quiz_controller',
    __name__,
    template_folder='views',
    url_prefix='/quiz'
)


@quiz_controller.before_request
@login_required
def before_request():
    pass


# Quiz/Question_1
@quiz_controller.route('/question-1', methods=['GET'])
def question_1():
    """
    Quiz Question 1
    """

    return render_template(
        'question.jinja2',
        question_number=str(1)
    )
