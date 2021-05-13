from flask import Blueprint, jsonify
from flask import current_app as app

subjects = [
    'Requirements Engineering',
    'Spezifikation',
    'Financial Services Management',
    'Mathematik I',
    'Mathematik II'
]

api_v1_controller = Blueprint(
    'api_v1_controller',
    __name__,
    url_prefix='/api/v1/'
)


@api_v1_controller.route('getAllSubjects', methods=['GET'])
def get_all_subjects():
    return jsonify(subjects)
