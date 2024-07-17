import flask

def media_(file):
    return flask.send_from_directory('media', file)