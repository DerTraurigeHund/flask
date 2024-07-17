import flask

def static_(file):
    return flask.send_from_directory('static', file)