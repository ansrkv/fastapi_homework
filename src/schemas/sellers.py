from pydantic import BaseModel

class SellerBase(BaseModel):
    first_name :str
    last_name:str
    email: str

class IncomingSeller(SellerBase):
    password:str

class ReturnedSeller(SellerBase):
    id:int

class ReturnedAllSellers(BaseModel):
    sellers:list[ReturnedSeller]