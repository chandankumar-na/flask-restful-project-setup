from flask import Blueprint
from flask_restful import Api

from demoapp.resources.HelloWorld import HelloWorldResource

api_bp=Blueprint('api',__name__)
api=Api(api_bp)

#Route
api.add_resource(HelloWorldResource,'/hello')