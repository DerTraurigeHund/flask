import flask

def login_():
    if 'username' in flask.session:
        return flask.redirect('/')
    print(flask.session)
    return flask.render_template('login.html')