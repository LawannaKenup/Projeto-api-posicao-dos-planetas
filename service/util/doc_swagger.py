from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'planeta1': fields.String(required=True, description="Planeta"),
    'planeta2': fields.String(required=True, description="Planeta observado")})
