# Library and Package imports
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

# Local imports
from init import db
from models import TestModel, CompanyModel, ProjectModel
from schemas import TestSchema, TestAndProjectSchema
from decorators import admin_required


test_blp = Blueprint("Test", "test", description="Operations on Test for "
                                              "Projects")

@test_blp.route("/company/<string:company_id>/test")
class TestsInCompany(MethodView):
    """Test Requested by Company

    Class TestsInCompany resource. It contains methods for handling
    HTTP GET and POST requests at the /company/<company_id>/test endpoint.
    """
    @test_blp.response(200, TestSchema(many=True))
    def get(self, company_id):
        """Get List of Tests requested by Company:

        Method handles the HTTP GET request at the
        /company/<company_id>/test endpoint.

        Args:
            company_id (str): The ID of the company to retrieve tests for.

        Returns:
            list: A list of all tests in the company.
        """
        company = CompanyModel.query.get_or_404(company_id)

        return company.tests.all()

    @test_blp.arguments(TestSchema)
    @test_blp.response(201, TestSchema)
    def post(self, test_data, company_id):
        """Create a new Test for a Company:

        Method handles the HTTP POST request at the
        /company/<company_id>/test endpoint.

        Args:
            test_data (dict): The data of the new test to be created.
            company_id (str): The ID of the company to create the test for.

        Returns:
            TestModel: The newly created test.

        Raises:
            HTTPException: If a test with the same name already exists in the company (HTTP 400)
                           or if an error occurred when creating the test (HTTP 500).
        """
        # if TestModel.query.filter(TestModel.company_id == company_id,
        #                          TestModel.name == test_data["name"]).first():
        #     abort(400,
        #           message="A Test with that name already exists in that "
        #                   "Company.")

        test = TestModel(**test_data, company_id=company_id)

        try:
            db.session.add(test)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return test


@test_blp.route("/project/<string:project_id>/test/<string:test_id>")
class LinkTestToProject(MethodView):
    """Linking Test to Project Resource:

    Class represents the LinkTestToProject resource. It contains methods for handling
    HTTP POST and DELETE requests at the /project/<project_id>/test/<test_id> endpoint.
    """
    @test_blp.response(201, TestSchema)
    def post(self, project_id, test_id):
        """Link a Project in a Company to a Test in the same Company:

        Method handles the HTTP POST request at the
        /project/<project_id>/test/<test_id> endpoint.

        Args:
            project_id (str): The ID of the project to link the test to.
            test_id (str): The ID of the test to link to the project.

        Returns:
            TestModel: The linked test.

        Raises:
            HTTPException: If an error occurred when linking the test to the project (HTTP 500).
        """
        project = ProjectModel.query.get_or_404(project_id)
        test = TestModel.query.get_or_404(test_id)

        project.tests.append(test)

        try:
            db.session.add(project)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while adding this Test.")

        return test

    @jwt_required()
    @admin_required
    @test_blp.doc(security=[{"jwt": []}])
    @test_blp.response(200, TestAndProjectSchema)
    def delete(self, project_id, test_id):
        """Unlink Test from a Project:

        Method handles the HTTP DELETE request at the
        /project/<project_id>/test/<test_id> endpoint.

        Args:
            project_id (str): The ID of the project to unlink the test from.
            test_id (str): The ID of the test to unlink from the project.

        Returns:
            dict: A message indicating the test was unlinked from the project, and the project and test data.

        Raises:
            HTTPException: If an error occurred when unlinking the test from the project (HTTP 500).
        """
        project = ProjectModel.query.get_or_404(project_id)
        test = TestModel.query.get_or_404(test_id)

        project.tests.remove(test)

        try:
            # project.tests.remove(test)
            db.session.add(project)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while adding the Test.")

        return {"message": "Project removed from Test", "project": project, "test": test}


@test_blp.route("/test/<string:test_id>")
class Test(MethodView):
    """Test Resource:

    class represents the Test resource. It contains methods for handling
    HTTP GET and DELETE requests at the /test/<test_id> endpoint.
    """
    @test_blp.response(200, TestSchema)
    def get(self, test_id):
        """Get info on a Test by ID:

        Method handles the HTTP GET request at the /test/<test_id> endpoint.

        Args:
            test_id (str): The ID of the test to retrieve.

        Returns:
            TestModel: The test with the given ID.

        Raises:
            HTTPException: If a test with the given ID does not exist (HTTP 404).
        """
        test = TestModel.query.get_or_404(test_id)
        return test

    # Swagger UI documentation
    @test_blp.response(
        202,
        description="Deletes a Test if no Project is associated with it.",
        example={"message": "Test deleted."},
    )
    @test_blp.alt_response(
        404,
        description="Test not found."
    )
    @test_blp.alt_response(
        400,
        description="Returned if the Test is assigned to one or more "
                    "projects. In this case, the Test is not deleted.",
    )


    @jwt_required()
    @admin_required
    @test_blp.doc(security=[{"jwt": []}])
    def delete(self, test_id):
        """Delete a Test by ID:

        Method handles the HTTP DELETE request at the /test/<test_id>
        endpoint. Deletes the test with the given ID if it is not associated
        with any projects.

        This endpoint requires JWT authentication and admin privileges. The JWT token
        should be provided in the 'Authorization' header as a Bearer token.

        In the Swagger-UI, you can click on the 'Authorize' button and enter your JWT
        token to authenticate after login. The token will be included in the
        'Authorization' header for all requests made from the Swagger UI.

        Args:
            test_id (str): The ID of the test to delete.

        Returns:
            dict: A message indicating the test was deleted.

        Raises:
            HTTPException: If a test with the given ID does not exist (HTTP 404)
                           or if the test is associated with any projects (HTTP 400).
        """
        test = TestModel.query.get_or_404(test_id)

        if not test.projects:
            db.session.delete(test)
            db.session.commit()
            return {"message": "Test deleted."}
        abort(
            400,
            message="Could not delete Test. Make sure Test is not associated "
                    "with any Projects, then try again.",
        )