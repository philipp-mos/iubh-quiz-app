from flask import current_app as app
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required

from ...models.quizgame.QuizGame import QuizGame
from ...models.quizgame.QuizGameResult import QuizGameResult
from ...models.quizgame.QuizGameStatus import QuizGameStatus

from .viewmodels.QuizQuestionViewModel import QuizQuestionViewModel
from .viewmodels.QuizGameResultViewModel import QuizGameResultViewModel

from ...services.abstracts.AbcQuizService import AbcQuizService
from ...services.QuizService import QuizService


__quizservice: AbcQuizService = QuizService()

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

    quiz_game: QuizGame = __quizservice.initialize_quiz_game_for_subject(subject_id)

    session['CURRENT_QUIZ_ID'] = quiz_game.id
    session['CURRENT_QUIZ_RESULT_ID'] = 0

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
    quiz_game_id = session.get('CURRENT_QUIZ_ID')

    if not quiz_game_id:
        raise ValueError

    viewmodel = QuizQuestionViewModel()

    if request.method == 'POST':

        if not viewmodel.is_validation_step.data:
            __quizservice.save_quiz_game_question_score(
                quiz_game_id,
                question_number,
                viewmodel
            )

        if app.config.get('SHOW_QUESTIONRESULTS_ONLY_SUMMARIZED'):
            return redirect(url_for('quiz_controller.question', question_number=question_number + 1))

        if viewmodel.is_validation_step.data:
            if question_number == app.config.get('AMOUNT_OF_QUESTIONS_PER_QUIZ'):
                return redirect(url_for('quiz_controller.question_results'))

            return redirect(url_for('quiz_controller.question', question_number=question_number + 1))

        viewmodel.is_validation_step.data = True

    if question_number == (app.config.get('AMOUNT_OF_QUESTIONS_PER_QUIZ') + 1):
        return redirect(url_for('quiz_controller.question_results'))

    __quizservice.fill_quizquestionviewmodel_by_quizgame_id(viewmodel, int(quiz_game_id), question_number)

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
    quiz_game_id = session.get('CURRENT_QUIZ_ID')

    if not quiz_game_id:
        raise ValueError

    __quizservice.update_quiz_game_status_to(quiz_game_id, QuizGameStatus.FINISHED)

    quizgame_result: QuizGameResult = __quizservice.save_and_get_quiz_game_result(quiz_game_id)

    viewmodel = QuizGameResultViewModel()
    viewmodel.amount_questions = quizgame_result.amount_of_questions
    viewmodel.amount_correct_questions = quizgame_result.amount_of_correct_questions

    return render_template(
        'results.jinja2',
        viewmodel=viewmodel
    )


# Quiz/Question/Results
@quiz_controller.route('/game/overview', methods=['GET'])
def game_overview():
    """
    Returns the Overview of QuizGames to use
    """
    viewmodel = []

    viewmodel = QuizService.get_played_games_for_quiz_game_overview()

    return render_template(
        'game_overview.jinja2',
        viewmodel=viewmodel
    )
