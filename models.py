from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class CRMData(Base):
    __tablename__ = "crm_data"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)


# Pydantic model for response in required format
class CRMDataSchema(BaseModel):
    id: int
    data: dict

    class Config:
        orm_mode = True
        from_attributes=True


class MarketingData(Base):
    __tablename__ = "marketing_data"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)


# Pydantic model for response in required format
class MarketingDataSchema(BaseModel):
    id: int
    data: dict

    class Config:
        orm_mode = True
        from_attributes=True

