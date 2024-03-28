# Libraries and package imports
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


# Local imports
from init import db
from models import CompanyModel
from schemas import CompanySchema
from decorators import admin_required


company_blp = Blueprint("Company", __name__, description="Operations on "
                                                   "Engineering Companies")

@company_blp.route("/company")
class CompanyList(MethodView):
    """CompanyList Resource:

    Class CompanyList resources. Contains methods for handling
    HTTP GET and POST requests at the /company endpoint.
    """
    @company_blp.response(200, CompanySchema(many=True))
    def get(self):
        """Get list of all Companies:

        Method handles the HTTP GET request at the /company endpoint.

        Returns:
            list: A list of all companies in the database.
        """
        return CompanyModel.query.all()


    @company_blp.arguments(CompanySchema)
    @company_blp.response(201, CompanySchema)
    def post(self, company_data):
        """Create New Company:

        Method to handle the HTTP POST request at the /company endpoint.

        Args:
            company_data (dict): The data of the new company to be created.

        Returns:
            CompanyModel: The newly created company.

        Raises:
            HTTPException: If a company with the same name already exists (HTTP 400)
                           or if an error occurred when creating the company (HTTP 500).
        """
        company = CompanyModel(**company_data)
        try:
            db.session.add(company)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A Company with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the Company.")

        return company


@company_blp.route("/company/<string:company_id>")
class Company(MethodView):
    """Company Resource:

    Class Company resources. Contains methods for handling
    HTTP GET and DELETE requests at the /company/<company_id> endpoint.
    """
    @company_blp.response(200, CompanySchema)
    def get(self, company_id):
        """Get Company by ID:

        Method handles the HTTP GET request at the /company/<company_id>
        endpoint.

        Args:
            company_id (str): The ID of the company to retrieve.

        Returns:
            CompanyModel: The company with the given ID.

        Raises:
            HTTPException: If a company with the given ID does not exist (HTTP 404).
        """
        company = CompanyModel.query.get_or_404(company_id)
        return company


    @jwt_required()
    @admin_required
    @company_blp.doc(security=[{"jwt": []}])
    def delete(self, company_id):
        """Delete Company by ID:

        Method handles the HTTP DELETE request at the /company/<company_id>
        endpoint.

        Args:
            company_id (str): The ID of the company to delete.

        Returns:
            dict: A message indicating the company was deleted.

        Raises:
            HTTPException: If a company with the given ID does not exist (HTTP 404).
        """
        company = CompanyModel.query.get_or_404(company_id)
        db.session.delete(company)
        db.session.commit()
        return {"message": "Company deleted"}, 200


