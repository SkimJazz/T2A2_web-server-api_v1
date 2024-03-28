from init import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    is_admin = db.Column(db.Boolean, default=False)

    # Foreign key to companies table
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    # Relationship to CompanyModel
    company = db.relationship('CompanyModel', back_populates='users')