from typing import List

from flask import Blueprint, render_template
from flask_login import login_required

from ... import cache_manager

from ...models.subject.Subject import Subject

from ...repositories.SubjectRepository import SubjectRepository

from ...services.SubjectService import SubjectService


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

    all_subjects: List[Subject] = cache_manager.get_from_key(cache_manager._GETALLSUBJECTSORDEREDBYNAME)

    if not all_subjects:
        all_subjects = cache_manager.set_by_key(
            cache_manager._GETALLSUBJECTSORDEREDBYNAME,
            SubjectRepository.get_all_ordered_by_name(),
            cache_manager._ONEDAY
        )

    return render_template(
        'overview.jinja2',
        subjects=SubjectService.subjectlist_to_subjectoverviewviewmodellist_mapping(all_subjects)
    )
