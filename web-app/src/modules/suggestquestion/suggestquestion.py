from flask import Blueprint, render_template, session, request, redirect, url_for
from flask_login import login_required

from .viewmodels.SubjectSelectionViewModel import SubjectSelectionViewModel
from .viewmodels.QuestionAndAnswerViewModel import QuestionAndAnswerViewModel


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
@suggestquestion_controller.route('/subject-selection', methods=['GET', 'POST'])
def subjectselection():
    """
    Question-Suggest First Page
    """
    subject_selection_viewmodel = SubjectSelectionViewModel()

    if session.get('quizsuggest__subject_id') and session.get('quizsuggest__subject_name'):
        subject_selection_viewmodel.subject_id.data = session.get('quizsuggest__subject_id')
        subject_selection_viewmodel.subject_name.data = session.get('quizsuggest__subject_name')


    if request.method == 'POST' and subject_selection_viewmodel.validate_on_submit():
        session['quizsuggest__subject_id'] = subject_selection_viewmodel.subject_id.data
        session['quizsuggest__subject_name'] = subject_selection_viewmodel.subject_name.data

        return redirect(url_for('suggestquestion_controller.questionandanswer'))



    return render_template(
        'subjectselection.jinja2',
        form=subject_selection_viewmodel
    )


## SuggestQuestion/QuestionAndAnswer ##
@suggestquestion_controller.route('/question-and-answer', methods=['GET'])
def questionandanswer():
    """
    Question-Suggest Second Page
    """
    questionandanswer_viewmodel = QuestionAndAnswerViewModel()

    return render_template(
        'questionandanswer.jinja2',
        form=questionandanswer_viewmodel
    )


## SuggestQuestion/Thanks ##
@suggestquestion_controller.route('/thanks', methods=['GET'])
def thanks():
    """
    Question-Suggest Third Page
    """

    return render_template('thanks.jinja2')
