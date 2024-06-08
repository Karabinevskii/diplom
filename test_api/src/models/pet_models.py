from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    pet_id: int
    name: str


class Tag(BaseModel):
    pet_id: int
    name: str


class PetModel(BaseModel):
    pet_id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str
