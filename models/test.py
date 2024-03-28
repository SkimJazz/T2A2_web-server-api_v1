from init import db


class TestModel(db.Model):
    __tablename__ = "tests"

    # Primary key for Tests table
    id = db.Column(db.Integer, primary_key=True)

    # Attributes for Tests table
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=True)
    test_type = db.Column(db.String(80), unique=False, nullable=True)
    test_method = db.Column(db.String(80), unique=False, nullable=True)

    # Foreign key relationship to companies table
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)

    # One-to-many relationship tests and companies
    company = db.relationship("CompanyModel", back_populates="tests")
    # Many-to-many relationship projects and tests
    projects = db.relationship("ProjectModel", back_populates="tests", secondary="projects_tests")
