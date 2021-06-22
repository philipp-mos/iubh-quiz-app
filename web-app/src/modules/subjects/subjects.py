from flask import Blueprint, render_template
from flask_login import login_required

from ...repositories.SubjectRepository import SubjectRepository

from .viewmodels.SubjectOverviewViewModel import SubjectOverviewViewModel

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


# Subjects/Overview
@subjects_controller.route('/overview', methods=['GET'])
def overview():
    """
    Subjects Overview
    """

    all_subjects = SubjectRepository.get_all_ordered_by_name()

    subjectviewmodel = []

    for subject in all_subjects:
        subjectviewmodel.append(
            SubjectOverviewViewModel(
                subject.name,
                subject.short,
                subject.image_path
            )
        )

    return render_template(
        'overview.jinja2',
        subjects=subjectviewmodel
    )
