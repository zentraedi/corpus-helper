from flask import Blueprint, redirect, url_for, abort, render_template

# Define the blueprint
entry_point = Blueprint('dashboard', __name__)

# Set the route and accepted methods
@entry_point.route('/', methods=['GET'])
def index():
    try:
        return redirect(url_for('dashboard.dashboard'))
    except Exception as e:
        raise e
        abort(404)


@entry_point.route('/dashboard', methods=['GET'])
def dashboard():
    # js = render_template('dashboard/index.js')
    return render_template('dashboard/index.html', title='Dashboard')
