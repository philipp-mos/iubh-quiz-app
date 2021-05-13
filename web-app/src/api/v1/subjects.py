from flask import Blueprint, jsonify
from ...models.subject import Subject


subjects = [
    Subject('Requirements Engineering'),
    Subject('Spezifikation'),
    Subject('Financial Services Management'),
    Subject('Mathematik I'),
    Subject('Mathematik II')
]

api_v1__subjects_controller = Blueprint(
    'api_v1__subjects_controller',
    __name__,
    url_prefix='/api/v1/subjects/'
)


@api_v1__subjects_controller.route('', methods=['GET'])
def get_all():
    return jsonify(
        {'subjects': list(map(lambda x: x.json(), subjects))}
    )
