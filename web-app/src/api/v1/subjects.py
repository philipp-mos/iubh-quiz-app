from flask import Blueprint, jsonify

from .dtos.SubjectDto import SubjectDto

from ...repositories.SubjectRepository import SubjectRepository

api_v1__subjects_controller = Blueprint(
    'api_v1__subjects_controller',
    __name__,
    url_prefix='/api/v1/subjects'
)


@api_v1__subjects_controller.route('/', methods=['GET'])
def get_all():

    all_subjects = SubjectRepository.get_all()

    subject_dto_list = []

    for subject in all_subjects:
        subject_dto_list.append(
            SubjectDto(subject.id, subject.name)
        )


    return jsonify(
        {'subjects': list(map(lambda x: x.json(), subject_dto_list))}
    )
