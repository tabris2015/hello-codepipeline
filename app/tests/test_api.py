from fastapi.testclient import TestClient
from app.main import app
import boto3
from moto import mock_dynamodb
from app.db import get_table


def override_get_table():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.create_table(
        TableName="mock-table",
        KeySchema=[
            {"AttributeName": "username", "KeyType": "HASH"},  # Partition key
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "username",
                # AttributeType defines the data type. "S" is string type and "N" is number type
                "AttributeType": "S",
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10,  # WriteCapacityUnits set to 10 writes per second
        },
    )
    return table


app.dependency_overrides[get_table] = override_get_table

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "built with codebuild", "stage": "local"}


@mock_dynamodb
def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []


@mock_dynamodb
def test_create_user():
    user = {
        "username": "test_user",
        "first_name": "test",
        "last_name": "user",
        "age": 90,
        "alias": "chupacabras",
    }
    response = client.post("/users/", json=user)
    assert response.status_code == 201
    assert response.json() == user


@mock_dynamodb
def test_fail_create_invalid_user():
    user = {
        "username": "test_user",
        "last_name": "user",
        "age": 90,
        "alias": "chupacabras",
    }
    response = client.post("/users/", json=user)
    assert response.status_code == 422
    # assert response.json() == user


@mock_dynamodb
def test_create_user_with_optional_fields():
    user = {
        "username": "test_user",
        "first_name": "test",
        "last_name": "user",
        "age": None,
        "alias": None,
    }
    response = client.post("/users/", json=user)
    assert response.status_code == 201
    assert response.json() == user
