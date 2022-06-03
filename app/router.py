from typing import List
import json
from fastapi import APIRouter, Depends
from app.models import User
from app.db import get_table
from app.notification import get_sns_client, sns_topic_arn

user_router = APIRouter()


@user_router.post("/", response_model=User, status_code=201)
def create_user(user: User, table=Depends(get_table)):
    table.put_item(Item=user.dict())
    return user


@user_router.get("/", response_model=List[User])
def list_users(limit: int = 100, table=Depends(get_table)):
    response = table.scan(Limit=limit)
    return [User(**item) for item in response["Items"]]


@user_router.delete("/")
def delete_user(username: str, table=Depends(get_table), sns_client=Depends(get_sns_client)):
    table.delete_item(Key={"username": username})
    sns_client.publish(
        TargetArn=sns_topic_arn,
        Message=json.dumps({"default": json.dumps({"message": f"user {username} deleted!"})})
    )
    return {"message": "OK"}
