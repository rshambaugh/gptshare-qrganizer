from sqlalchemy import Column, Integer, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class QRCode(Base):
    __tablename__ = 'qr_codes'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=False), server_default=func.now())
