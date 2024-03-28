from init import db


class ProjectTest(db.Model):
    __tablename__ = "projects_tests"

    # Primary key for ProjectsTests table
    id = db.Column(db.Integer, primary_key=True)

    # Foreign key relationships to projects and tests tables
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    test_id = db.Column(db.Integer, db.ForeignKey("tests.id"))