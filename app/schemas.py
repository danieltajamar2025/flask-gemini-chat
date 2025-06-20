from marshmallow import Schema, fields, ValidationError

class RegisterSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=lambda x: len(x) >= 6 if x else False)

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class ChatSchema(Schema):
    content = fields.Str(required=True)

def validate_json(schema_class):
    def decorator(f):
        def wrapper(*args, **kwargs):
            from flask import request, jsonify
            try:
                json_data = request.get_json()
                if not json_data:
                    return jsonify({'error': 'No JSON data provided'}), 400
                
                schema = schema_class()
                data = schema.load(json_data)
                return f(data, *args, **kwargs)
            except ValidationError as err:
                return jsonify({'errors': err.messages}), 400
            except Exception as e:
                return jsonify({'error': f'Validation error: {str(e)}'}), 400
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator