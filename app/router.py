from typing import List
from fastapi import APIRouter
from models import User
from db import table

user_router = APIRouter()


@user_router.post("/", response_model=User)
def create_user(user: User):
    table.put_item(Item=user.dict())
    return user


@user_router.get("/", response_model=List[User])
def list_users(limit: int = 100):
    response = table.scan(Limit=limit)
    return [User(**item) for item in response["Items"]]
