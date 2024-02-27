from fastapi import APIRouter, Depends, Query
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import CRMData, MarketingData,CRMDataSchema,MarketingDataSchema
from utils import common,db

#api call starts from here
router = APIRouter()

'''
 * Get Marketing & CRM Data with pagination limit 10 as default
 * @route GET /data
 * @returns JSON Object 200 - Ok
 * @returns JSON Object 500 - Internal server error
'''
@router.get("/data")
async def get_data(offset: int = 0, limit: int = 10, session: AsyncSession = Depends(db.get_session)):
    crm_data = await session.execute(select(CRMData).offset(offset).limit(limit))
    marketing_data = await session.execute(select(MarketingData).offset(offset).limit(limit))
    # Fetch all data in dictionary format
    crm_data_list = [CRMDataSchema.from_orm(record).dict() for record in crm_data.scalars().all()]
    marketing_data_list = [MarketingDataSchema.from_orm(record).dict() for record in marketing_data.scalars().all()]
    return common.process_success_response({"crm_data": crm_data_list,"marketing_data": marketing_data_list})




