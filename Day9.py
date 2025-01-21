# from fastapi import FastAPI
# import random

# app = FastAPI()

# @app.get('/')  # main endpoint ->> "/" = path
# async def root():  # every time user loads this will be the first response user gets
#     return {'example': "this is an example", "data": 0}

# @app.get('/random1')
# async def get_random1():
#     number = random.randint(0, 100)
#     return {'number': number, 'limit': 100}

# @app.get('/random/{limit}')
# async def get_random_limit(limit: int):
#     number1 = random.randint(0, limit)
#     return {'number': number1, 'limit': limit}

from flask import Flask, request,jsonify
app = Flask(__name__)
@app.route("/")#@vaneko decorator
def home():
    return "Home"
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data ={
        "user_id":user_id,
        "name":"Nischal ",
        "email":"nischal@example.com"

    }
    extra =request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data),200


@app.route("/create-user",methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data),201

def home():
    return "Home"
#Http methods like:
# GET:Request data from specific resource
# POST :Create a resource
# PUT: update a resource
# DELETE:delete a resource

if __name__ =="__main__":
    app.run(debug=True)

