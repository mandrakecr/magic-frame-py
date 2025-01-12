from datetime import timedelta

from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt
from sqlalchemy.exc import IntegrityError

from .models import User
from .schemas import UserInputSchema, UserLoginInputSchema
from common.database import db
from common.encryption import encryption_manager
from common.flask_hooks import validate_input
from common.jwt import token_required

bp = Blueprint('auth', __name__)


@bp.route('/', methods=['GET'])
def auth_root():
    return make_response(jsonify({'message': 'test route'}), 200)


@bp.route('/login', methods=['POST'])
@validate_input(UserLoginInputSchema())
def auth_login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = db.session.query(User).filter(User.email == email).first()
    if user and encryption_manager.check_password_hash(user.password, password):
        access_token = create_access_token(
            identity=str(user.id),
            fresh=True,
            expires_delta=timedelta(hours=48)
        )
        return jsonify({'access_token': access_token})
    else:
        return {'message': 'Invalid email or password'}, 401


@bp.route('/register', methods=['POST'])
@validate_input(UserInputSchema())
def auth_register():
    email = request.json.get("email")
    password = request.json.get("password")
    hash = encryption_manager.generate_password_hash(password).decode("utf-8")
    new_user = User(email=email, password=hash)

    try:
        db.session.add(new_user)
        db.session.flush()
    except IntegrityError as error:
        db.session.rollback()
        return make_response(jsonify({'message': 'User already exists'}), 400)

    return make_response(jsonify({'message': 'User registered successfully'}), 201)


@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200


@bp.route('/me', methods=['GET'])
@token_required
def me():
    current_user_id = get_jwt_identity()
    token_info = get_jwt()
    return jsonify(user=current_user_id, info=token_info)


def register_routes(app):
    app.register_blueprint(bp)
