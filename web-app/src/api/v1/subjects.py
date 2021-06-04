from flask import Blueprint, jsonify, request

from .dtos.SubjectDto import SubjectDto

from ...repositories.SubjectRepository import SubjectRepository

api_v1__subjects_controller = Blueprint(
    'api_v1__subjects_controller',
    __name__,
    url_prefix='/api/v1/subjects'
)


@api_v1__subjects_controller.route('/', methods=['GET'])
def get():

    all_subjects = SubjectRepository.get_all()

    subject_dto_list = []

    for subject in all_subjects:
        subject_dto_list.append(
            SubjectDto(subject.id, subject.name)
        )


    return jsonify(
        {'subjects': list(map(lambda x: x.json(), subject_dto_list))}
    )


@api_v1__subjects_controller.route('/search', methods=['GET'])
def search():

    search_arguments = request.args

    if 'query' in search_arguments:
        query = search_arguments['query']


    subject_search_result = SubjectRepository.search_by_query(query)

    subject_dto_list = []

    for subject in subject_search_result:
        subject_dto_list.append(
            SubjectDto(subject.id, subject.name)
        )


    return jsonify(
        {'subjects': list(map(lambda x: x.json(), subject_dto_list))}
    ), 200
