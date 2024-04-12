from users.schemas import UserSchema, UserSchemaIn

REGISTER_SWAGGER = {
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': 'Новый пользователь',
            'schema': UserSchema(many=False)
        }
    }
}
