from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = ["vidhuran","jhon"]

class User(BaseModel):
    name:str

@app.get("/user")
def get_user():
    return {"users":users}

@app.post("/users")
def add_users(user:User):
    users.append(user.name)
    return {
        "message":"user added",
        "users": users
    }
    