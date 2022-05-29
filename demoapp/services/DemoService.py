from demoapp.Model import db,User,UserSchema
user_schema=UserSchema(many=True)

class DemoService:
    
    def create_user(self,data):
        try:
            user=User(name=data['name'],email=data['email'])
            result=db.session.add(user)
            db.session.commit()
        except KeyError as e:
            print(e)
        return result
    
    def get_users(self):
        users=User.query.all()
        users=user_schema.dump(users)
        return users
    
    def delete_user(self):
        result=db.session.execute("DELETE FROM User")
        db.session.commit()
        return result

