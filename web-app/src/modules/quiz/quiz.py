from flask import current_app as app
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required

from ...models.subject.Subject import Subject
from ...models.quizgame.QuizGame import QuizGame
from ...models.quizgame.QuizGameQuestion import QuizGameQuestion
from ...models.quizgame.QuizGameQuestionAnswer import QuizGameQuestionAnswer

from .viewmodels.QuizQuestionViewModel import QuizQuestionViewModel

from ...repositories.SubjectRepository import SubjectRepository
from ...repositories.QuizGameRepository import QuizGameRepository

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

    quiz_game: QuizGame = QuizService.initialize_quiz_game_for_subject(subject_id)

    session['CURRENT_QUIZ_ID'] = quiz_game.id

    return redirect(url_for('quiz_controller.question', question_number=1))


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

    app.logger.info('Session QuizId: ' + str(session.get('CURRENT_QUIZ_ID')))

    if request.method == 'POST' and viewmodel.validate_on_submit():
        if question_number == app.config.get('AMOUNT_OF_QUESTIONS_PER_QUIZ'):
            return redirect(url_for('quiz_controller.question_results'))

        return redirect(url_for('quiz_controller.question', question_number=question_number + 1))

    if not session.get('CURRENT_QUIZ_ID'):
        raise ValueError

    quiz_game: QuizGame = QuizGameRepository.find_by_id(session.get('CURRENT_QUIZ_ID'))

    if not quiz_game:
        raise ValueError

    subject: Subject = SubjectRepository.find_by_id(quiz_game.subject_id)

    if not subject:
        raise ValueError

    viewmodel.subject_name = subject.name

    quiz_game_question: QuizGameQuestion = quiz_game.quizgamequestions[question_number - 1]

    viewmodel.question_text = quiz_game_question.quizquestion_text

    viewmodel.question_number = question_number

    viewmodel.answers = {}

    for quizgame_answer in quiz_game_question.quizgamequestionanswers:
        viewmodel.answers[chr(ord('@') + quizgame_answer.position)] = quizgame_answer.quizanswer_text

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
