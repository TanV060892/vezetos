from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models import CRMData
from utils import common,db

#api call starts from here
router = APIRouter()

'''
 * Webhook Endpoint
 * @route POST /webhook
 * @returns JSON Object 200 - Ok
 * @returns JSON Object 422 - Unprocessable Entity
 * @returns JSON Object 500 - Internal server error
'''
@router.post("/webhook")
async def receive_webhook(data: dict, session: AsyncSession = Depends(db.get_session)):
    new_data = CRMData(data=data)
    session.add(new_data)
    await session.commit()
    return common.process_success_response({"message": "Data received"})


