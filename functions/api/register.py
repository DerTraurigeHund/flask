import functions.common_operations as common
import hashlib
import flask
import datetime


def api_register():
    post_data = flask.request.get_json()

    username = post_data['username']
    password = post_data['password']
    email = post_data['email']
    
    # Check if username or password is empty
    if not username or not password or not email:
        return {"success": False, "message": "Username, email and password required"}
    
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if the username already exists
    existing_user = common.select_mysql_command(f"SELECT * FROM `users` WHERE `username` = '{username}' OR `email` = '{email}'")
    
    if existing_user:
        return {"success": False, "message": "Username or email already exists"}
    
    # Insert the new user into the database
    try:
        common.run_mysql_command(f"INSERT INTO `users` (`username`, `password`, `email`, `created_at`) VALUES ('{username}', '{hashed_password}', '{email}', '{datetime.datetime.now()}')")
        return {"success": True, "message": "User registered successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}