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



## SuggestQuestion/SubjectSelection ##
@suggestquestion_controller.route('/subject-selection', methods=['GET'])
def subjectselection():
    """
    Question-Suggest First Page
    """

    return render_template('subjectselection.jinja2')


## SuggestQuestion/QuestionAndAnswer ##
@suggestquestion_controller.route('/question-and-answer', methods=['GET'])
def questionandanswer():
    """
    Question-Suggest Second Page
    """

    return render_template('questionandanswer.jinja2')
