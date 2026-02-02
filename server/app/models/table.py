from sqlalchemy import Text, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..db.postgres import Base
from .enum import TaskStatus
from enum import Enum


class Task(Base):
   __tablename__ = "tasks"

   id: Mapped[int] = mapped_column(primary_key=True)

   title: Mapped[str] = mapped_column(
      String(200),
      nullable=False
   )

   description: Mapped[str | None] = mapped_column(
      Text
   )

   status: Mapped[TaskStatus] = mapped_column(
      Enum(TaskStatus, name="task_status_enum"),
      nullable=False,
      default=TaskStatus.PENDING
   )

   user_id: Mapped[int] = mapped_column(
      ForeignKey("users.id", ondelete="CASCADE"),
      nullable=False
   )

   user: Mapped["User"] = relationship(
      backref="tasks"
   )
