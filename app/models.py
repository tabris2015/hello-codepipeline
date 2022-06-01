from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str  # Partition key!
    first_name: str
    last_name: str
    age: Optional[int]
    alias: Optional[str]
