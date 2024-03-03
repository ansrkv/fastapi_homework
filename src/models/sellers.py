from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, ForeignKey


class Seller(BaseModel):
    __tablename__ = 'sellers'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    email:Mapped[str] = mapped_column()
    password:Mapped[str] = mapped_column()
    books = relationship("Book", back_populates="seller")
