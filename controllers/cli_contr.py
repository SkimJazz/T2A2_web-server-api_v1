# Libraries and package imports
from flask_smorest import Blueprint
from passlib.hash import pbkdf2_sha256

# Local imports
from init import db
from models.company import CompanyModel
from models.project import ProjectModel
from models.test import TestModel
from models.project_test import ProjectTest
from models.user import UserModel


db_commands = Blueprint("db", __name__)


@db_commands.cli.command('create')
def create_tables():
    """Create tables in the database:

    Function command for the Flask application's command-line interface (CLI),
    registered under the 'create' command.

    This command creates all tables defined in the SQLAlchemy models in the
    database. This is done using the 'create_all()' method of the SQLAlchemy
    'db' instance.

    Confirmation message "Tables created" is printed to the console.

    Usage:
        Run 'flask db create' in the terminal to execute this command.
    """
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    """Drop tables from the database:

    Function command for the Flask application's command-line interface (CLI),
    registered under the 'drop' command.

    This command allows the tester to drop all tables defined in the SQLAlchemy
    models from the database if shit goes astray! This is done using the
    'drop_all()' method of the SQLAlchemy 'db' instance.

    After the tables are dropped, a confirmation message "Tables dropped"
    is outputted to the console.

    Usage:
        Run 'flask db drop' in the terminal to execute this command.
    """
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    """ Seed tables in the database:

    Function command for the Flask application's command-line interface (CLI),
    registered under the 'seed' command.

    This command will seed the database with initial data for users, companies,
    projects, tests, and project_tests. This is done by creating instances
    of the respective SQLAlchemy models and adding them to the database session.

    After data is added, the session is committed to the database.

    This function also hashes the passwords for the users using the
    'pbkdf2_sha256' hashing algorithm from the 'passlib' library.

    Upon seeded the tables, a confirmation message "Tables seeded" is
    outputted to the console.

    Usage:
        Run 'flask db seed' in the terminal to execute this command.
    """

    companies = [
        CompanyModel(
            name="Soil Surveys Pty Ltd",
            registration_number="NHU1664DIV",
            industry_sector="Geotechnical Engineering",
            services="Soil Testing",
        )
    ]
    db.session.add_all(companies)
    db.session.commit()


    users = [
        UserModel(
            username="Admin",
            email="admin@email.com.au",
            password=pbkdf2_sha256.hash("123456"),
            is_admin=True,
            # company_id=companies[0].id

    ),
        UserModel(
            username="User 1",
            email="user1@email.com.au",
            password=pbkdf2_sha256.hash("123456"),
            company_id=companies[0].id
        )
    ]
    db.session.add_all(users)
    db.session.commit()


    projects = [
        ProjectModel(
            name="Retaining Wall Failure",
            budget="56000",
            description="Epic retaining wall failure",
            client="Brisbane City Council",
            company_id=companies[0].id
        )
    ]
    db.session.add_all(projects)


    tests = [
        TestModel(
            name="Dynamic Cone Penetrometer (DCP) assessment",
            description="DCP test to determine soil strength",
            test_type="Geotechnical",
            test_method="AS1289.6.3.1",
            company_id=companies[0].id
        )
    ]
    db.session.add_all(tests)
    db.session.commit()


    projects_tests = [
        ProjectTest(
            project_id=projects[0].id,
            test_id=tests[0].id
        )
    ]
    db.session.add_all(projects_tests)
    db.session.commit()
    print("Tables seeded")

