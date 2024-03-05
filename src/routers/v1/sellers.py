from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.configurations.database import get_async_session
from src.models.sellers import Seller
from src.schemas.sellers import IncomingSeller, ReturnedAllSellers, ReturnedSeller, SellerBase



sellers_router = APIRouter(tags=["sellers"], prefix="/sellers")


DBSession = Annotated[AsyncSession, Depends(get_async_session)]


@sellers_router.post("/")
async def create_seller(
    seller: IncomingSeller, session: DBSession
):
    new_seller = Seller(
        first_name=seller.first_name,
        last_name=seller.last_name,
        email=seller.email,
        password=seller.password,
    )
    session.add(new_seller)
    await session.flush()

    return Response(status_code=status.HTTP_201_CREATED)


@sellers_router.get("/", response_model=ReturnedAllSellers)
async def get_all_sellers(session: DBSession):
    query = select(Seller)
    res = await session.execute(query)
    sellers = res.scalars().all()
    return {"sellers":sellers}


@sellers_router.get("/{seller_id}", response_model=ReturnedSeller)
async def get_seller(seller_id: int, session: DBSession):
    res = await session.get(Seller, seller_id)
    return res


@sellers_router.delete("/{seller_id}", response_model=ReturnedSeller)
async def delete_seller(seller_id: int, session: DBSession):
    deleted_seller = await session.get(Seller, seller_id)
    if deleted_seller:
        await session.delete(deleted_seller)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@sellers_router.put("/{seller_id}", response_model=ReturnedSeller)
async def update_seller(seller_id: int, new_data: SellerBase, session: DBSession):
    if seller := await session.get(Seller, seller_id):
        seller.first_name = new_data.first_name
        seller.last_name = new_data.last_name
        seller.email = new_data.email

        await session.flush()

        return seller

    return Response(status_code=status.HTTP_404_NOT_FOUND)
