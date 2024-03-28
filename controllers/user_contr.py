# Libraries and package imports
from datetime import timedelta
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)

# Local imports
from init import db
from models import UserModel
from schemas import UserSchema


user_blp = Blueprint("Users", __name__, description="Operations on users")


# --------------------------- USER REGISTRATION ---------------------------- #

@user_blp.route("/register")
class UserRegister(MethodView):
    """User Register Resource:

    Class UserRegister resources. Contains a method for handling
    HTTP POST requests at the /register endpoint.
    """
    @user_blp.arguments(UserSchema)
    def post(self, user_data):
        """Register a new user:

        Method handles the HTTP POST request at the /register endpoint.

        Args:
            user_data (dict): The data of the new user to be registered.

        Returns:
            dict: A message indicating the user was created successfully.

        Raises:
            HTTPException: If a user with the same username already exists (HTTP 409).
        """
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
            email=user_data["email"],
            is_admin=user_data.get("is_admin", False),
            company_id=user_data.get("company_id", None)
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201



# --------------------------- USER LOGIN ----------------------------------- #

@user_blp.route("/login")
class UserLogin(MethodView):
    """User Login Resource:

    Class UserLogin resource. Contains a method for handling
    HTTP POST requests at the /login endpoint.
    """
    @user_blp.arguments(UserSchema)
    def post(self, user_data):
        """login a User or Admin:

        Method handles the HTTP POST request at the /login endpoint.

        Args:
            user_data (dict): The data of the user to be logged in.

        Returns:
            dict: An access token for the logged in user.

        Raises:
            HTTPException: If the username or password is incorrect (HTTP 401).
        """
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]).first()

        # Check if the user exists and the password is correct:
        #   For the body of the if statement to run, the user must exist then
        #   verify the password making sure it is valid.
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            # Pass in the user's identity in which case is the user's ID
            additional_claims = {"is_admin": user.is_admin}
            # access_token = create_access_token(identity=user.id, fresh=True)
            access_token = create_access_token(identity=user.id,
                                               additional_claims=additional_claims,
                                               expires_delta=timedelta(seconds=300),
                                               fresh=True)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")



# -------------- TESTING ONLY - NOT FOR PRODUCTION APP --------------------- #

@user_blp.route("/user/<int:user_id>")
class User(MethodView):
    """TESTING ONLY:

    Testing class for Getting user by ID and Deleting user by ID.

    Useful when testing the Flask app before production. May not want to
    expose it to public users, or they may delete each other's accounts!

    DELETE out this class before deploying!
    """
    @user_blp.response(200, UserSchema)
    def get(self, user_id):
        """Get user by ID:

        Method handles the HTTP GET request at the /user/<user_id> endpoint.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            UserModel: The user with the given ID.

        Raises:
            HTTPException: If a user with the given ID does not exist (HTTP 404).
        """
        # user = UserModel.query.get_or_404(user_id)
        user = UserModel.query.get(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        return user


    @jwt_required()
    @user_blp.doc(security=[{"jwt": []}])
    def delete(self, user_id):
        """Delete user by ID:

        Method handles the HTTP DELETE request at the /user/<user_id> endpoint.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            dict: A message indicating the user was deleted.

        Raises:
            HTTPException: If the current user is not an admin (HTTP 403)
                           or if the current user is trying to delete themselves (HTTP 403)
                           or if a user with the given ID does not exist (HTTP 404).
        """
        current_user_id = get_jwt_identity()
        current_user = UserModel.query.get(current_user_id)

        # user = UserModel.query.get_or_404(user_id)
        if not current_user.is_admin:
            abort(403, message="Only admins can delete users.")

        # Prevent admins from deleting themselves
        if current_user_id == user_id:
            abort(403,
                  message="Oops! You can't delete yourself!. Ask the "
                          "Superuser to do it for you."
                  )

        user = UserModel.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200