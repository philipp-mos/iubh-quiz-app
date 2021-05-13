from flask import Blueprint, jsonify

subjects = [
    'Requirements Engineering',
    'Spezifikation',
    'Financial Services Management',
    'Mathematik I',
    'Mathematik II'
]

api_v1__subjects_controller = Blueprint(
    'api_v1__subjects_controller',
    __name__,
    url_prefix='/api/v1/subjects/'
)


@api_v1__subjects_controller.route('', methods=['GET'])
def get_all():
    return jsonify(subjects)
