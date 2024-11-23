from pydantic import BaseModel
from datetime import datetime

class QRCodeBase(BaseModel):
    data: str

class QRCodeCreate(QRCodeBase):
    pass

class QRCode(QRCodeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode: True
