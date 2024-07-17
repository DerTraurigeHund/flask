import flask
import flask.sessions
import flask_socketio
from routs import load_routes
import json


config = json.loads(open('config.json', 'r').read())

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

app.config['SECRET_KEY'] = config['flask_config']['secret_key']
app.permanent_session_lifetime  = True

socketio.init_app(app)
load_routes(app, socketio)