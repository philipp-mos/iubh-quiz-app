from flask import Blueprint, jsonify


api_v1__highscore_controller = Blueprint(
    'api_v1__highscore_controller',
    __name__,
    url_prefix='/api/v1/highscore'
)


@api_v1__highscore_controller.route('/update', methods=['GET'])
def update():
    """
    Run the Highscore Calculation and Update Entries
    """

    return jsonify(
        {'status': 'success'}
    ), 200
