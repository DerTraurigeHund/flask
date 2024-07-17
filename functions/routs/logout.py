import flask

def logout_():
    if 'username' in flask.session:
        flask.session.pop('username')
        flask.session.pop('user_id')
    return flask.redirect('/login')