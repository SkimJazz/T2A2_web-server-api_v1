# library and Package imports
import os
from flask_smorest import Api
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
#import secrets     # For generating random secret key

# Local imports
from init import db
from controllers.comp_contr import company_blp
from controllers.proj_contr import project_blp
from controllers.test_contr import test_blp
from controllers.user_contr import user_blp
from controllers.cli_contr import db_commands


def create_app():
    """App Factory Function:

    This function is responsible for creating and configuring the Flask
    application.

    It sets up the configuration for the Flask application, OpenAPI,
    SQLAlchemy, JWT, and registers the blueprints.

    Returns:
        app: The configured Flask application.
    """
    app = Flask(__name__)
    load_dotenv()
    app.json.sort_keys = False  # Flask DON'T sort JSON keys


    # -------- OpenAPI Configuration and Swagger UI documentation ----------- #

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "GeoLabs API"
    app.config["API_VERSION"] = "v0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config['OPENAPI_SECURITY_DEFINITIONS'] = {
        "jwt": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # http://127.0.0.1:5000/swagger-ui
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    # --------------------- Database Configuration -------------------------- #

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # Deprecated


    # ------------- Initialized Flask SQLAlchemy extension ------------------ #
    # Take flask app as argument & connect it to SQLAlchemy
    db.init_app(app)
    api = Api(app)


    # --------------------------- JWT CONFIGURATION ------------------------- #

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)


    # JWT error handling token loaders work with the @jwt_required() decorator
    #   when testing the API with SWAGGER-UI, the token is sent in the header
    #   of the "Authorize" dialog box as "jwt (http, Bearer)" value: and the
    #   token is validated by the @jwt_required() decorator. If the token is
    #   invalid, expired or missing, the error handlers are called and the
    #   appropriate error message is returned to the user. Timedelta in
    #   user_contr for /login is set at 300 seconds (5 minutes) for testing
    #   purposes. REF jwt loaders below:


    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        """If Token is expired:

        Callback function that is called when a JWT token has expired.

        Args:
            jwt_header: The header of the JWT.
            jwt_payload: The payload of the JWT.

        Returns:
            A tuple containing a JSON response and a status code.
        """
        return (
            jsonify({"message": "The token has expired.",
                     "error": "token_expired"}),
            401,
        )


    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        """If Token is invalid:

        Callback function that is called when a JWT token is invalid.

        Args:
            error: The error message.

        Returns:
            A tuple containing a JSON response and a status code.
        """
        return (
            jsonify(
                {"message": "Signature verification failed.",
                 "error": "invalid_token"}
            ),
            401,
        )


    @jwt.unauthorized_loader
    def missing_token_callback(error):
        """If Token is missing:

        Callback function that is called when a JWT token is missing.

        Args:
            error: The error message.

        Returns:
            A tuple containing a JSON response and a status code.
        """
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )


    # OpenAPI swagger-ui docs authorization security scheme for JWT
    api.spec.components.security_scheme("jwt", {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    })


    # --------------------------- END JWT CONFIGURATION --------------------- #

    # Don't need the following if using Flask-Migrate for database migrations.
    # with app.app_context():
        # Create all tables in database:
        #db.create_all()

        # Drop all tables in database:
        #   To drop all tables you must uncomment the 'db.drop_all()' and comment
        #   out 'db.create_all()' and run the app once. Then comment out 'db.drop_all()'
        #   and uncomment 'db.create_all()' and run the app again. This will let
        #   you create all tables from scratch. Use when test seeding data into
        #   database before using CLI commands to seed the tables.
        #db.drop_all()


    # ---------------------- Blueprint Rego's ------------------------------- #
    api.register_blueprint(user_blp)
    api.register_blueprint(company_blp)
    api.register_blueprint(project_blp)
    api.register_blueprint(test_blp)
    api.register_blueprint(db_commands)  # Shows as 'db' in Swagger-UI


    return app