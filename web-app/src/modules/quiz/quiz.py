from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from .viewmodels.QuizQuestionViewModel import QuizQuestionViewModel


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


# Quiz/Question
@quiz_controller.route('/question', methods=['GET'])
def question_fallback():
    """
    Fallback Route for Question-Action without Parameter
    """
    return redirect(url_for('quiz_controller.question', question_number=1))


# Quiz/Question/{question_number}
@quiz_controller.route('/question/<int:question_number>', methods=['GET', 'POST'])
def question(question_number: int):
    """
    Quiz Question
    """
    viewmodel = QuizQuestionViewModel()

    if request.method == 'POST' and viewmodel.validate_on_submit():
        return redirect(url_for('quiz_controller.question', question_number=question_number + 1))

    viewmodel.question_text = 'Lorem ipsum dolor sit amet?'

    viewmodel.question_number = question_number

    viewmodel.answers = {
        'A': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'B': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'C': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }

    return render_template(
        'question.jinja2',
        viewmodel=viewmodel
    )
