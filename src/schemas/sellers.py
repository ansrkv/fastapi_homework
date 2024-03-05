from pydantic import BaseModel
from src.schemas.books import ReturnedBook

class SellerBase(BaseModel):
    first_name :str
    last_name:str
    email: str

class IncomingSeller(SellerBase):
    password:str

class ReturnedSeller(SellerBase):
    id:int
    books:list[ReturnedBook]

class ReturnedAllSellers(BaseModel):
    sellers:list[ReturnedSeller]
