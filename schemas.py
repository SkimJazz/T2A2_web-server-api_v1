from marshmallow import Schema, fields


# Plain Project Schema. No information about the company.
class PlainProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    budget = fields.Float(required=True)
    description = fields.Str()
    client = fields.Str(required=True)


class PlainCompanySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    registration_number = fields.Str(required=True)
    industry_sector = fields.Str(required=True)
    services = fields.Str(required=True)


class PlainTestSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    test_type = fields.Str()
    test_method = fields.Str()


class ProjectUpdateSchema(Schema):
    name = fields.Str()
    budget = fields.Float()
    description = fields.Str()


class ProjectSchema(PlainProjectSchema):
    company_id = fields.Int(required=True, load_only=True)
    company = fields.Nested(PlainCompanySchema(), dump_only=True)   # Return company info to the user
    tests = fields.List(fields.Nested(PlainTestSchema()), dump_only=True)


class CompanySchema(PlainCompanySchema):
    projects = fields.List(fields.Nested(PlainProjectSchema()), dump_only=True)
    # tests = fields.List(fields.Nested(PlainTestSchema()), dump_only=True)


class TestSchema(PlainTestSchema):
    company_id = fields.Int(load_only=True)
    projects = fields.List(fields.Nested(PlainProjectSchema()), dump_only=True)
    company = fields.Nested(PlainCompanySchema(), dump_only=True)


class TestAndProjectSchema(Schema):
    message = fields.Str()
    project = fields.Nested(ProjectSchema)
    test = fields.Nested(TestSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    is_admin = fields.Bool(dump_only=True)
    company = fields.Nested(PlainCompanySchema(), dump_only=True)
    company_id = fields.Int(load_only=True)

