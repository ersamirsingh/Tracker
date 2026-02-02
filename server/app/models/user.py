from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM
from ..db.postgres import Base
from .enum import UserRole




class User(Base):
   __tablename__ = "users"

   id: Mapped[int] = mapped_column(primary_key=True)

   name: Mapped[str] = mapped_column(String(100), nullable=False)

   email: Mapped[str] = mapped_column(
      String(150),
      unique=True,
      index=True,
      nullable=False
   )

   role: Mapped[UserRole] = mapped_column(
      ENUM(UserRole, name="user_role_enum"),
      nullable=False,
      default=UserRole.USER
   )

   is_active: Mapped[bool] = mapped_column(
      Boolean,
      default=True
   )
