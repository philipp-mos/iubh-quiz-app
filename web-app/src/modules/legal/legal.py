from flask import Blueprint, render_template


legal_controller = Blueprint(
    'legal_controller',
    __name__,
    template_folder='views',
    url_prefix='/legal'
)


## Legal/Imprint ##
@legal_controller.route('/imprint', methods=['GET'])
def imprint():
    """
    Imprint-View.
    Content is delivered by Google Tag Manager
    """
    return render_template('imprint.jinja2')


## Legal/PrivacyPolicy ##
@legal_controller.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    """
    PrivacyPolicy-View.
    Content is delivered by Google Tag Manager
    """
    return render_template('privacypolicy.jinja2')
