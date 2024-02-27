import asyncio
import httpx
from utils import db
from models import CRMData, MarketingData

API_KEY = "TanV060892"

async def sync_crm_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://challenge.berrydev.ai/api/crm/customers",
            headers={"X-API-Key": API_KEY}, timeout=60.0
        )
        data = response.json()
        async with db.async_session() as session:
            for customer in data.get("customers", []):
                crm_data = CRMData(data=customer)
                session.add(crm_data)
            await session.commit()

async def sync_marketing_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://challenge.berrydev.ai/api/marketing/campaigns",
            headers={"X-API-Key": API_KEY}, timeout=60.0
        )
        data = response.json()
        async with db.async_session() as session:
            for campaign in data.get("campaigns", []):
                marketing_data = MarketingData(data=campaign)
                session.add(marketing_data)
            await session.commit()
