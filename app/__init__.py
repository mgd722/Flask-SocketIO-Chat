from flask import Flask
from flask_socketio import SocketIO

# does not work
socketio = SocketIO(message_queue='redis://')

# does work
# socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # does not work
    socketio.init_app(app)

    # does work
    # socketio.init_app(app, message_queue='redis://')

    return app

