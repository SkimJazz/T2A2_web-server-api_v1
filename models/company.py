from init import db


class CompanyModel(db.Model):
    __tablename__ = "companies"

    # Primary key for Companies table
    id = db.Column(db.Integer, primary_key=True)

    # Attributes for Companies table
    name = db.Column(db.String(80), unique=True, nullable=False)
    registration_number = db.Column(db.String(80), unique=True, nullable=False)
    industry_sector = db.Column(db.String(80), nullable=False)
    services = db.Column(db.String(80), nullable=False)


    # One-to-many relationship companies and projects
    projects = db.relationship("ProjectModel", back_populates="company", lazy="dynamic")

    # One-to-many relationship companies and tests
    tests = db.relationship("TestModel", back_populates="company", lazy="dynamic")

    # One-to-many relationship companies and users
    users = db.relationship("UserModel", back_populates="company", lazy="dynamic")
