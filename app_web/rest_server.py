from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from app_web.db import db_session
from app_web.controllers import return_all_users, return_user, return_all_routes_of_user, return_route_of_user
from app_web.controllers import return_point_of_route, return_all_routes, insert_route, return_one_route
from app_web.controllers import return_score_of_route, end_route, return_user_stats, return_routes_stats
from app_web.controllers import check_user_route_combo, check_route_point_combo
from pprint import pprint

app = Flask(__name__, static_url_path='', static_folder='/')
CORS(app, resources={r"/*": {"origins": "*"}})

##################
#                #
# /api/users/... #
#                #
##################

@app.route('/api/users', methods=['GET'])
def users_all():
    users, status = return_all_users()
    return jsonify(users), status

# args ==> inlcude_routes --> include_scores, include_profile
@app.route('/api/users/<user_id>', methods=['GET'])
def user_one(user_id):
    user, status = return_user(db_session, user_id, request.args)
    return jsonify(user), status

# args ==> inlcude_scores
@app.route('/api/users/<user_id>/routes', methods=['GET'])
def user_one_routes_all(user_id):
    routes, status = return_all_routes_of_user(db_session, user_id, request.args)
    return jsonify(routes), status

# args ==> include_labels, include_score
@app.route('/api/users/<user_id>/routes/<route_id>', methods=['GET'])
def user_one_route_one(user_id, route_id):
    msg, status = return_user(db_session, user_id, request.args)
    if status != 200:
        return jsonify(msg), status
    msg, status = check_user_route_combo(user_id, route_id)
    if status != 200:
        return jsonify(msg), status
    route, status = return_route_of_user(db_session, route_id, request.args)
    return jsonify(route), status

@app.route('/api/users/<user_id>/routes/<route_id>/<score_id>', methods=['GET'])
def user_one_route_one_score(user_id, route_id, score_id):
    msg, status = return_user(db_session, user_id, request.args)
    if status != 200:
        return jsonify(msg), status
    msg, status = check_user_route_combo(user_id, route_id)
    if status != 200:
        return jsonify(msg), status
    msg, status = check_route_point_combo(route_id, score_id)
    if status != 200:
        return jsonify(msg), status
    score, status = return_point_of_route(score_id)
    return jsonify(score), status

###################
#                 #
# /api/routes/... #
#                 #
###################

# args ==> active
@app.route('/api/routes', methods=['GET', 'POST'])
def routes_all():
    if request.method == 'GET':
        routes, status = return_all_routes(db_session, request.args)
        return jsonify(routes), status
    else:
        route_data = request.get_json()
        msg, status = insert_route(db_session, route_data)
        return jsonify(msg), status

# args ==> include_labels, include_score
@app.route('/api/routes/<route_id>', methods=['GET', 'POST'])
def route_one(route_id):
    if request.method == 'GET':
        route, status = return_one_route(db_session, route_id, request.args)
        return jsonify(route), status
    else:
        msg, status = end_route(db_session, route_id)
        return jsonify(msg), status

##################
#                #
# /api/stats/... #
#                #
##################

@app.route('/api/stats/users', methods=['GET'])
def stats_users():
    user_stats, status = return_user_stats(db_session)
    return jsonify(user_stats), status

@app.route('/api/stats/routes', methods=['GET'])
def stats_routes():
    average_profile, status = return_routes_stats(db_session)
    return jsonify(average_profile), status

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response

def main():
    # app.run(host='localhost', port=6969)
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()