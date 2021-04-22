from pprint import pprint

from sqlalchemy.sql.functions import user
from app_web.db import Profile, db_session, User, Route, Score, Profile
from app_web.functionalities import obj_to_dict, list_of_obj_to_dict, sql_row_to_dict, list_of_sql_rows_to_dict, list_of_floats_to_list_of_percentages
from sqlalchemy.orm import load_only
from sqlalchemy import and_, func
import datetime

##################
#                #
# /api/users/... #
#                #
##################

def return_all_users():
    users = User.query.order_by(User.lastname.asc()).all()
    users = list_of_obj_to_dict(users)
    return {'users': users}, 200

def return_user(db_session, user_id, args):
    try:
        user_id = int(user_id)
    except Exception as e:
        return {'msg': 'Invalid user id'}, 400
    user = User.query.filter(User.user_id == user_id).options(load_only('firstname', 'lastname')).all()
    if len(user) == 0:
        return {'msg': 'User not found'}, 404
    else:
        user = user[0]
    user = obj_to_dict(user)
    if 'include_routes' in args:
        routes, _ = return_all_routes_of_user(db_session, user_id, args)
        user['routes'] = routes['routes'] 
    if 'include_profile' in args:
        query ='''  select profile, count(score_id) as cnt from scores, profiles
                    where scores.aggressive_score > profiles.lower and scores.aggressive_score <= profiles.upper
	                    and scores.route_id in (
		                    select route_id
		                    from users, routes 
		                    where users.user_id=routes.user_id and users.user_id={0}
                        )
                    group by profile '''.format(user_id)
        results = db_session.execute(query)
        results = [(row['profile'], row['cnt']) for row in results]
        percentages = list_of_floats_to_list_of_percentages([score_count[1] for score_count in results])
        if len(results) > 0:
            profile = {results[i][0]: percentages[i] for i in range(0, len(percentages))}
        else:
            profile = {}
        user['profile'] = profile
    return user, 200

def return_all_routes_of_user(db_session, user_id, args):
    try:
        user_id = int(user_id)
    except Exception as e:
        return {'msg': 'Invalid user id'}, 400
    user = User.query.filter(User.user_id == user_id).options(load_only('firstname', 'lastname')).all()
    if len(user) == 0:
        return {'msg': 'User not found'}, 404
    routes = Route.query.filter(Route.user_id == user_id).order_by(Route.date.desc())\
        .options(load_only('route_id', 'date', 'is_active')).all()
    routes = list_of_obj_to_dict(routes)
    if 'include_scores' in args:
        for i in range(0, len(routes)):
            routes[i]['score'] = return_score_of_route(db_session, routes[i]['route_id'])
    return {'routes': routes}, 200

def return_route_of_user(db_session, route_id, args):
    exist_route = Route.query.filter(Route.route_id == route_id).all()
    if len(exist_route) == 0:
        return {'msg': 'Route not found'}, 404
    res = {}
    res['is_active'] = exist_route[0].is_active
    if 'include_labels' in args:
        route = return_route_of_user_labeled(db_session, route_id)
    else:
        scores = Score.query.filter(Score.route_id == route_id).order_by(Score.start_time.asc())\
            .options(load_only('score_id', 'start_time', 'end_time', 'aggressive_score', 'normal_score')).all()
        route = list_of_obj_to_dict(scores)
    res['route'] = route
    if 'include_score' in args:
        score = return_score_of_route(db_session, route_id)
        res['score'] = score
        count = return_count_of_route(db_session, route_id)
        res['count'] = count
    return res, 200
        
def return_route_of_user_labeled(db_session, route_id):
    routes = db_session.query(
            Score.score_id, 
            Score.start_time, Score.end_time,
            Score.aggressive_score, Score.normal_score,
            Profile.profile)\
        .filter(and_(Score.aggressive_score > Profile.lower, Score.aggressive_score <= Profile.upper, Score.route_id == route_id))\
        .order_by(Score.start_time.asc()).all()
    return list_of_sql_rows_to_dict(['score_id', 'start_time', 'end_time', 'aggressive_score', 'normal_score', 'profile'], routes)

def check_user_route_combo(user_id, route_id):
    try:
        user_id = int(user_id)
    except Exception as e:
        return {'msg': 'Invalid user id'}, 400
    res = Route.query.filter(and_(Route.route_id == route_id, Route.user_id == user_id)).all()
    if len(res) == 0:
        return {'msg': 'This user does not have a route with this id'}, 404
    return {'msg': 'ok'}, 200

def check_route_point_combo(route_id, score_id):
    try:
        score_id = int(score_id)
    except Exception as e:
        return {'msg': 'Invalid score id'}, 400
    res = Score.query.filter(and_(Score.route_id == route_id, Score.score_id == score_id)).all()
    if len(res) == 0:
        return {'msg': 'This route does not have a point with this id'}, 404
    return {'msg': 'ok'}, 200

def return_score_of_route(db_session, route_id):
    score_counts = db_session.query(Profile.profile, func.count(Score.score_id))\
        .filter(and_(Score.aggressive_score > Profile.lower, Score.aggressive_score <= Profile.upper, Score.route_id == route_id))\
        .group_by(Profile.profile).all()
    percentages = list_of_floats_to_list_of_percentages([score_count[1] for score_count in score_counts])
    try:
        score = {score_counts[i][0]: percentages[i] for i in range(0, len(percentages))}
    except IndexError as e:
        score = {}
    return score

def return_count_of_route(db_session, route_id):
    score_counts = db_session.query(Profile.profile, func.count(Score.score_id))\
        .filter(and_(Score.aggressive_score > Profile.lower, Score.aggressive_score <= Profile.upper, Score.route_id == route_id))\
        .group_by(Profile.profile).all()
    try:
        counts = {score_counts[i][0]: score_counts[i][1] for i in range(0, len(score_counts))}
    except IndexError as e:
        counts = {}
    return counts

def return_point_of_route(score_id):
    try:
        score_id = int(score_id)
    except Exception as e:
        return {'msg': 'Invalid score id'}, 400
    score = Score.query.filter(Score.score_id == score_id)\
        .options(load_only('start_time', 'end_time', 'aggressive_score', 'normal_score')).all()
    if len(score) == 0:
        return {'msg': 'Point of route not found'}, 404
    else:
        score = score[0]
    return obj_to_dict(score), 200

###################
#                 #
# /api/routes/... #
#                 #
###################

def return_all_routes(db_session, args):
    if 'active' in args:
        routes = db_session.query(User.user_id, User.firstname, User.lastname, Route.route_id, Route.date, Route.is_active)\
            .filter(and_(User.user_id == Route.user_id, Route.is_active == 1))\
            .order_by(Route.date.desc()).all()
    else:
        routes = db_session.query(User.user_id, User.firstname, User.lastname, Route.route_id, Route.date, Route.is_active)\
            .filter(User.user_id == Route.user_id)\
            .order_by(Route.date.desc()).all()
    routes = list_of_sql_rows_to_dict(['user_id', 'firstname', 'lastname', 'route_id', 'date', 'is_active'], routes)
    return {'routes': routes}, 200

def return_one_route(db_session, route_id, args):
    return return_route_of_user(db_session, route_id, args)

def insert_route(db_session, route_dict):
    try:
        new_route = Route(route_id=route_dict['route_id'], user_id=route_dict['driver_id'],\
            date=datetime.datetime.strptime(route_dict['date'], '%Y-%m-%d %H:%M:%S'), is_active=route_dict['is_active'])
        db_session.add(new_route)
        db_session.commit()
        msg = 'Route inserted'
        status = 201
    except KeyError as e:
        msg = 'Wrong JSON body error'
        status = 400
    except Exception as e:
        msg = 'Internal server error'
        status = 500
    return {'msg': msg}, status

def end_route(db_session, route_id):
    try:
        db_session.query(Route).filter(Route.route_id == route_id)\
            .update({Route.is_active: 0}, synchronize_session='fetch')
        db_session.commit()
        msg = 'Route stopped'
        status = 200
    except Exception as e:
        msg = 'Internal server error'
        status = 500
    return {'msg': msg}, status

##################
#                #
# /api/stats/... #
#                #
##################

def return_user_stats(db_session):
    all_users, _ = return_all_users()
    user_ids = [d['user_id'] for d in all_users['users']]
    user_profiles = [d['profile'] for d, _ in [return_user(db_session, user_id, {'include_profile': ''}) for user_id in user_ids]]
    total_users = len(user_ids)
    normal_users = sum([1 for user_profile in user_profiles if user_profile.get('NORMAL')])
    slightly_aggressive_users = sum([1 for user_profile in user_profiles if user_profile.get('SLIGHTLY AGGRESSIVE')])
    fairly_aggressive_users = sum([1 for user_profile in user_profiles if user_profile.get('FAIRLY AGGRESSIVE')])
    highly_aggressive_users = sum([1 for user_profile in user_profiles if user_profile.get('HIGHLY AGGRESSIVE')])
    extremely_aggressive_users = sum([1 for user_profile in user_profiles if user_profile.get('EXTREMELY AGGRESSIVE')])
    return {
        'TOTAL': total_users, 'NORMAL': normal_users, 'SLIGHTLY AGGRESSIVE': slightly_aggressive_users,
        'FAIRLY AGGRESSIVE': fairly_aggressive_users, 'HIGHLY AGGRESSIVE': highly_aggressive_users,
        'EXTREMELY AGGRESSIVE': extremely_aggressive_users
    }, 200

def return_routes_stats(db_session):
    query ='''  select profile, count(score_id) as cnt from scores, profiles
                    where scores.aggressive_score > profiles.lower and scores.aggressive_score <= profiles.upper
	                    and scores.route_id in (
		                    select route_id
		                    from users, routes 
		                    where users.user_id=routes.user_id
                        )
                    group by profile '''
    results = db_session.execute(query)
    results = [(row['profile'], row['cnt']) for row in results]
    percentages = list_of_floats_to_list_of_percentages([score_count[1] for score_count in results])
    if len(results) > 0:
        profile = {results[i][0]: percentages[i] for i in range(0, len(percentages))}
    else:
        profile = {}
    return  profile, 200