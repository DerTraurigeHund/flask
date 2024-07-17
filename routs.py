import flask
import functions.routs as routs
import functions.api as api
# import functions.sockets as sockets
import colorama


GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
RESET = colorama.Fore.RESET

rout_list = {
    "html_sites": {
        ('/', routs.index_),
        ('/login', routs.login_),
    },

    "api_sites": {
        ('/api/login', api.api_login),
        ('/api/register', api.api_register),
    },

    "other_sites": {
        ('/static/<path:file>', routs.static_),
        ('/media/<path:file>', routs.media_),
        ('/logout', routs.logout_),
    },

    # "socket_events": {
    #     ('/connect', sockets.connect),
    #     ('/disconnect', sockets.disconnect),
    #     ('/login', sockets.login),
    # }
}


def load_routes(app, socketio):
    for route_type, options in rout_list.items():
        for route in rout_list[route_type]:
            try:
                if route_type == 'socket_events':
                    socketio.on_event(route[0], globals()[route[1]])
                    print(GREEN + f'   [+] Added {route_type[:-1].replace("_", " ")}: {route[0]}' + RESET)
                else:
                    app.add_url_rule(route[0], view_func=route[1], methods=['GET', 'POST'])
                    print(GREEN + f'   [+] Added {route_type[:-1].replace("_", " ")}: {route[0]}' + RESET)
            except Exception as e:
                print(RED + f'   [!] Cannot add {route_type[:-1].replace("_", " ")}: {route[0]} \n    [!] Error: {e}' + RESET)