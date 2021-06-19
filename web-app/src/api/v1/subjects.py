from flask import Blueprint, jsonify, request
from flask_login import login_required

from ...repositories.SubjectRepository import SubjectRepository
from ...services.SubjectService import SubjectService


api_v1__subjects_controller = Blueprint(
    'api_v1__subjects_controller',
    __name__,
    url_prefix='/api/v1/subjects'
)


@api_v1__subjects_controller.before_request
@login_required
def before_request():
    pass


@api_v1__subjects_controller.route('/', methods=['GET'])
def get():
    """
    Return all Subjects via DTO in JSON
    """

    subject_dto_list = SubjectService.subjectlist_to_subjectdtolist_mapping(
        SubjectRepository.get_all()
    )

    return jsonify(
        {'subjects': list(map(lambda x: x.json(), subject_dto_list))}
    ), 200


@api_v1__subjects_controller.route('/search', methods=['GET'])
def search():
    """
    Return all Subjects, that match to a given Search-Query, as DTO in JSON
    """

    search_arguments = request.args

    if 'query' in search_arguments:
        query = search_arguments['query']

    subject_dto_list = SubjectService.subjectlist_to_subjectdtolist_mapping(
        SubjectRepository.search_by_query(query, limit=5)
    )

    return jsonify(
        {'subjects': list(map(lambda x: x.json(), subject_dto_list))}
    ), 200
