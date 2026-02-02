import enum


class UserRole(enum.Enum):
   ADMIN = "admin"
   MANAGER = "manager"
   USER = "user"


class TaskStatus(enum.Enum):
   PENDING = "pending"
   IN_PROGRESS = "in_progress"
   DONE = "done"
   CANCELLED = "cancelled"
