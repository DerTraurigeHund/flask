import flask

def index_():
    if 'username' not in flask.session:
        return flask.redirect('/login')
    return flask.render_template('index.html')
