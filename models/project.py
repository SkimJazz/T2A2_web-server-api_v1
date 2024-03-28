from init import db


class ProjectModel(db.Model):
    __tablename__ = "projects"

    # Primary key for Projects table
    id = db.Column(db.Integer, primary_key=True)

    # Attributes for Projects table
    name = db.Column(db.String(80), unique=False, nullable=False)
    budget = db.Column(db.Float(precision=2), unique=False, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    client = db.Column(db.String(80), nullable=False)


    # Foreign key to companies table
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), unique=False, nullable=False)

    # One-to-many relationship with CompanyModel class
    company = db.relationship("CompanyModel", back_populates="projects")

    # Many-to-many relationship projects and tests
    tests = db.relationship("TestModel", back_populates="projects", secondary="projects_tests")
