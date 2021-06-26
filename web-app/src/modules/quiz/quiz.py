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


# Quiz/Question/{question_number}
@quiz_controller.route('/question/<int:question_number>', methods=['GET'])
def question(question_number: int):
    """
    Quiz Question
    """

    return render_template(
        'question.jinja2',
        question_number=str(question_number)
    )
