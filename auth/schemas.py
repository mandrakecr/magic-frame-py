from marshmallow import Schema, fields, validate


class UserLoginInputSchema(Schema):
    email = fields.Email(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)


class UserInputSchema(Schema):
    email = fields.Email(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)
