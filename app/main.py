import os
from fastapi import FastAPI
from mangum import Mangum
import boto3
from app.router import user_router
from app.db import table, table_name, dynamodb
from app.create_table import create_users_table

stage = os.environ.get("STAGE", "local")

app = FastAPI(
    title=f"Awesome API [{stage}]", root_path=None if stage == "local" else f"/{stage}"
)

app.include_router(user_router, prefix="/users")


@app.on_event("startup")
def check_table():
    print(hasattr(table, "status"))
    new_table = None
    if not hasattr(table, "status"):
        print("local env, creating table...")
        try:
            new_table = create_users_table(dynamodb, table_name)
        except boto3.client("dynamodb").exceptions.ResourceInUseException:
            print("Local table already exists!")


@app.get("/")
def root():
    """root endpoint"""
    return {"message": "built with codebuild", "stage": stage}


handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
