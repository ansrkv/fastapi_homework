from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, ForeignKey

class Book(BaseModel):
    __tablename__ = "books_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column()
    pages: Mapped[int] = mapped_column()
    seller_id= mapped_column(Integer, ForeignKey("sellers.id"))
    seller = relationship("Seller", back_populates="books")