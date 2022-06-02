from typing import List
from fastapi import APIRouter, Depends
from app.models import User
from app.db import get_table

user_router = APIRouter()


@user_router.post("/", response_model=User)
def create_user(user: User, table=Depends(get_table)):
    table.put_item(Item=user.dict())
    return user


@user_router.get("/", response_model=List[User])
def list_users(limit: int = 100, table=Depends(get_table)):
    response = table.scan(Limit=limit)
    return [User(**item) for item in response["Items"]]
