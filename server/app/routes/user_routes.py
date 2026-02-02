from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.postgres import get_db
from ..services.user_services import get_user

router = APIRouter(
   prefix="/users",
   tags=["Users"]
)


@router.get("/")
async def get_users(db: Session = Depends(get_db)):
   return get_user(db)

