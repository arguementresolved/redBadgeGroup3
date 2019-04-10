# from flask import request, json, Response, Blueprint, g
# from ..shared.authentication import Auth
# from ..models.battles import BattlesModel, BattlesSchema

# battles_api = Blueprint('battles', __name__)
# battles_schema = BattlesSchema()


# @battles_api.route('/', methods=['POST'])
# def create():
#     '''
#     Create endpoint for battles api
#     '''

#     req_data = request.get_json()
#     data, error = battles_schema.load(req_data)

#     if error:
#         return custom_response(error, 400)

#     # check if user already exists in db
#     battles_in_db = BattlesModel.get_user_by_email(data.get('email'))
#     if battles_in_db:
#         message = {'error': 'User already exists, please supply another email address'}
#         return custom_response(message, 400)

#     user = UserModel(data)
#     user.save()

#     ser_data = user_schema.dump(user).data

#     token = Auth.generate_token(ser_data.get('id'))

#     return custom_response({'token': token}, 201)


# @battles_api.route('/<int:fighter_id>', methods=['GET'])
# @Auth.auth_required
# def get_user(user_id):
#     '''
#     Get info from ID, off of the API
#     '''
#     fighter = BattlesModel.get_one_user(fighter_id)
#     if not figher:
#         return custom_response({'error': 'user not found'}, 404)

#     ser_user = user_schema.dump(user).data
#     return custom_response(ser_user, 200)


# @user_api.route('/me', methods=['GET'])
# @Auth.auth_required
# def get_me():
#     '''
#     Get owners user information (me)
#     '''

#     user = UserModel.get_one_user(g.user.get('id'))
#     ser_user = user_schema.dump(user).data
#     return custom_response(ser_user, 200)


# @user_api.route('/login', methods=['POST'])
# def login():
#     '''
#     Validates and returns a web token
#     if the user credentials are verified
#     '''
#     req_data = request.get_json()

#     data, error = user_schema.load(req_data, partial=True)

#     if error:
#         return custom_response(error, 400)

#     if not data.get('email') or not data.get('password'):
#         return custom_response({'error': 'email and password required to login'})

#     user = UserModel.get_user_by_email(data.get('email'))

#     if not user:
#         return custom_response({'error': 'invalid credentials'}, 400)

#     if not user.check_hash(data.get('password')):
#         return custom_response({'error': 'invalid credentials'})

#     ser_data = user_schema.dump(user).data

#     token = Auth.generate_token(ser_data.get('id'))

#     return custom_response({'token': token}, 200)


# @user_api.route('/me', methods=['PUT'])
# @Auth.auth_required
# def update():
#     '''
#     Allows owner of profile (me)
#     to update the user information
#     '''

#     req_data = request.get_json()
#     data, error = user_schema.load(req_data, partial=True)
#     if error:
#         return custom_response(error, 400)

#     user = UserModel.get_one_user(g.user.get('id'))
#     user.update(data)
#     ser_user = user_schema.dump(user).data
#     return custom_response(ser_user, 200)


# def custom_response(res, status_code):
#     '''
#     Creates a custom json response
#     for proper status messages
#     '''

#     return Response(
#         mimetype='application/json',
#         response=json.dumps(res),
#         status=status_code
#     )
