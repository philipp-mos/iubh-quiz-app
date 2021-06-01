from flask import Blueprint
from flask import render_template


legal_controller = Blueprint(
    'legal_controller',
    __name__,
    template_folder='views',
    url_prefix='/legal'
)


## Legal/Imprint ##
@legal_controller.route('/imprint', methods=['GET'])
def imprint():
    return render_template('imprint.jinja2')


## Legal/PrivacyPolicy ##
@legal_controller.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    return render_template('privacypolicy.jinja2')
