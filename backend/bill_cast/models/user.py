from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, Integer, String

from bill_cast.db.base_class import Base


if TYPE_CHECKING:
    from .deal import Deal
    from .shop import Shop


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
