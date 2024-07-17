from setup import socketio, app, config

if __name__ == '__main__':
    socketio.run(app, host=config['server']['host'], port=config['server']['port'], debug=True)