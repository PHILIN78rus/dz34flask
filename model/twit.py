from model.user import User

class Twit:

    def __init__(self, body: str, author: User):
        self.body = body
        self.author = author
    #def __dict__(self):
    #    return {"body": self.body, "author": self.author}
    

"""class MyClass:
    def __init__(self, x):
        self.x = x
 
    def __dict__(self):
        return {"x": self.x}
 
import json
obj = MyClass(5)
json.dumps(obj.__dict__)"""
