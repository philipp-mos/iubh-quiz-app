"""
Web Error-Handling
"""
from flask import render_template
from flask import current_app as app

def web_not_found(e):
    """Returns Web-404 Not Found Errorpage"""
    return render_template('errorpages/404.html'), 404


def web_server_error(e):
    """Returns Web-500 Server Error Errorpage"""
    return render_template('errorpages/500.html'), 500


app.register_error_handler(404, web_not_found)
app.register_error_handler(500, web_server_error)




"""
API Error-Handling
"""
from flask import jsonify
from ..api.v1.subjects import api_v1__subjects_controller

@api_v1__subjects_controller.errorhandler(500)
def api_server_error(e):
    """Returns Api-500 Server Error"""
    return jsonify(error=str(e)), 500
