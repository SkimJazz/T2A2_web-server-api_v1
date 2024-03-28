# Library and package imports
from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError


# Local imports
from init import db
from models import ProjectModel, CompanyModel
from schemas import ProjectSchema, ProjectUpdateSchema
from decorators import admin_required


project_blp = Blueprint("Project", __name__, description="Operations on "
                                                   "Engineering Projects")

@project_blp.route("/project/<string:project_id>")
class Project(MethodView):
    """Project Resources:

    Class Project resource. Contains methods for handling
    HTTP GET, DELETE, and PUT requests at the /project/<project_id> endpoint.
    """

    @project_blp.response(200, ProjectSchema)
    def get(self, project_id):
        """Get Project by ID:

        Method handles the HTTP GET request at the /project/<project_id>
        endpoint.

        Args:
            project_id (str): The ID of the project to retrieve.

        Returns:
            ProjectModel: The project with the given ID.

        Raises:
            HTTPException: If a project with the given ID does not exist (HTTP 404).
        """
        project = ProjectModel.query.get(project_id)
        if project is None:
            abort(404, message="Project does not exist.")
        return project

    @jwt_required()
    @admin_required
    @project_blp.doc(security=[{"jwt": []}])
    def delete(self, project_id):
        """Delete Project by ID:

        Method handles the HTTP DELETE request at the /project/<project_id>
        endpoint. Deletes the project with the given ID.

        This endpoint requires JWT authentication and admin privileges. The JWT token
        should be provided in the 'Authorization' header as a Bearer token.

        In the Swagger UI, you can click on the 'Authorize' button and enter your JWT
        token to authenticate after logining in. The token will be included in
        the 'Authorization' header for all requests made from the Swagger UI.

        Args:
            project_id (str): The ID of the project to delete.

        Returns:
            dict: A message indicating the project was deleted.

        Raises:
            HTTPException: If a project with the given ID does not exist (HTTP 404).
        """
        project = ProjectModel.query.get(project_id)

        # If project does not exist, return 404 with message
        if project is None:
            abort(404, message="Project does not exist.")

        db.session.delete(project)
        db.session.commit()
        return {"message": "Project deleted."}


    @project_blp.arguments(ProjectUpdateSchema)
    @project_blp.response(200, ProjectSchema)
    def put(self, project_data, project_id):
        """Update Project by ID:

        Method handles the HTTP PUT request at the /project/<project_id>
        endpoint.

        Args:
            project_data (dict): The updated data of the project.
            project_id (str): The ID of the project to update.

        Returns:
            ProjectModel: The updated project.

        Raises:
            HTTPException: If a project with the given ID does not exist (HTTP 404).
        """
        project = ProjectModel.query.get(project_id)

        if project:
            project.budget = project_data["budget"]
            project.name = project_data["name"]
            project.description = project_data["description"]
        else:
            project = ProjectModel(id=project_id, **project_data)

        db.session.add(project)
        db.session.commit()

        return project


@project_blp.route("/project")
class ProjectList(MethodView):
    """ProjectList Resource:

    Class ProjectList resource. Contains methods for handling
    HTTP GET and POST requests at the /project endpoint.
    """
    @project_blp.response(200, ProjectSchema(many=True))
    def get(self):
        """Get list of all Projects in database:

        Method handles the HTTP GET request at the /project endpoint.

        Returns:
            list: A list of all projects in the database.
        """
        return ProjectModel.query.all()


    @project_blp.arguments(ProjectSchema)
    @project_blp.response(201, ProjectSchema)
    def post(self, project_data):
        """Create New Project:

        This method handles the HTTP POST request at the /project endpoint.

        Args:
            project_data (dict): The data of the new project to be created.

        Returns:
            ProjectModel: The newly created project.

        Raises:
            HTTPException: If a project with the same name already exists in the same company (HTTP 400)
                           or if an error occurred when creating the project (HTTP 500).
        """
        # Check if company exists before creating it
        company = CompanyModel.query.get(project_data["company_id"])
        if not company:
            abort(400, message="Company does not exist.")

        # Check if project with same name exists in same company
        project = ProjectModel.query.filter_by(name=project_data["name"],
                                         company_id=project_data["company_id"],
                                         description=project_data["description"]).first()

        if project:
            abort(400,
                  message="A Project with that name already exists in the in this company.")

        project = ProjectModel(**project_data)

        try:
            db.session.add(project)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the project.")

        return project