from flask_restful import Resource
from flask import request
from demoapp.services.DemoService import DemoService

class HelloWorldResource(Resource):

    def __init__(self):
        self.service=DemoService()
        super().__init__()

    def get(self):
        args=request.args
        print(args)
        users=self.service.get_users()
        return {"message":"get working fine","data":users}
    
    def post(self):
        body=request.get_json()
        self.service.create_user(body)
        return {"message":"Post working fine","data":body}


