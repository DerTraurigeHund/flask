import functions.common_operations as common
import hashlib
import flask

def api_login():
    post_data = flask.request.get_json()

    username = post_data['username']
    password = post_data['password']

    password = hashlib.sha256(password.encode()).hexdigest()

    data = common.select_mysql_command(f"SELECT * FROM `users` WHERE `username` = '{username}' AND `password` = '{password}'")
    if data is [] or data is None or len(data) == 0:
        return {"success": False, "message": "Invalid username or password"}
    data = data[0]

    if data is None:
        return {"success": False, "message": "Invalid username or password"}

    if data is None or password != data[2] or username != data[1]:
        return {"success": False, "message": "Invalid username or password"}
    else:
        common.run_mysql_command(f"UPDATE `users` SET `last_login` = NOW() WHERE `username` = '{username}'")
        flask.session['username'] = username
        flask.session['user_id'] = data[0]
        return {"success": True, "username": username, "user_id": data[0]}