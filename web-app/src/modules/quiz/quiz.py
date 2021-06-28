from flask import current_app as app
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from .viewmodels.QuizQuestionViewModel import QuizQuestionViewModel

from ...services.QuizService import QuizService


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


# Quiz/Start
@quiz_controller.route('/start/<int:subject_id>', methods=['GET'])
def start(subject_id: int):
    """
    Initialize QuizGame and redirect to QuizGame
    """

    quiz_game = QuizService.initialize_quiz_game_for_subject(subject_id)

    return redirect(url_for('quiz_controller.question', question_number=1, quiz_game=quiz_game))


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
        if question_number == app.config.get('AMOUNT_OF_QUESTIONS_PER_QUIZ'):
            return redirect(url_for('quiz_controller.question_results'))

        return redirect(url_for('quiz_controller.question', question_number=question_number + 1))

    viewmodel.question_text = 'Lorem ipsum dolor sit amet?'

    viewmodel.question_number = question_number

    viewmodel.subject_name = 'Lorem ipsum dolor sit amet'

    viewmodel.answers = {
        'A': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'B': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'C': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }

    return render_template(
        'question.jinja2',
        viewmodel=viewmodel
    )


# Quiz/Question/Results
@quiz_controller.route('/question/results', methods=['GET'])
def question_results():
    """
    Final Step that shows the Quiz-Results
    """
    return render_template('results.jinja2')
