from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    firstname: str
    lastname: str
    password: str
    users_token: str

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    quantity: int

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity_select: int
