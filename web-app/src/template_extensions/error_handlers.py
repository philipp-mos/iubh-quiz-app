from flask import render_template
from flask import current_app as app


def not_found(e):
    """Returns 404 Not Found Errorpage"""
    return render_template('errorpages/404.html'), 404


def server_error(e):
    """Returns 500 Server Error Errorpage"""
    return render_template('errorpages/500.html'), 500




app.register_error_handler(404, not_found)
app.register_error_handler(500, server_error)