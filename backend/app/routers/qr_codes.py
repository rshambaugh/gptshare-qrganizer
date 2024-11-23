"""
Routes for QR code operations.

- POST /qr_codes/ : Create a new QR code.
- GET /qr_codes/{qr_code_id} : Retrieve a QR code by ID.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.models import QRCode
from app.schemas.schemas import QRCodeCreate, QRCode as QRCodeSchema
from app.core.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/qr_codes/", response_model=QRCodeSchema)
def create_qr_code(qr_code: QRCodeCreate, db: Session = Depends(get_db)):
    """
    Create a new QR code.

    Args:
        qr_code (QRCodeCreate): The data for the new QR code.
        db (Session): The database session.

    Returns:
        QRCode: The created QR code object.
    """
    db_qr_code = QRCode(data=qr_code.data)
    db.add(db_qr_code)
    db.commit()
    db.refresh(db_qr_code)
    return db_qr_code

@router.get("/qr_codes/{qr_code_id}", response_model=QRCodeSchema)
def read_qr_code(qr_code_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a QR code by ID.

    Args:
        qr_code_id (int): The ID of the QR code to retrieve.
        db (Session): The database session.

    Returns:
        QRCode: The requested QR code object, if found.

    Raises:
        HTTPException: If the QR code is not found.
    """
    db_qr_code = db.query(QRCode).filter(QRCode.id == qr_code_id).first()
    if db_qr_code is None:
    raise CustomHTTPException(status_code=404, detail='QR code not found')  # Custom exception
        raise HTTPException(status_code=404, detail="QR code not found")
    return db_qr_code

from typing import List
from app.schemas.schemas import QRCode as QRCodeSchema

@router.get("/qr_codes/", response_model=List[QRCodeSchema])
async def read_qr_codes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of QR codes with pagination.

    Args:
        skip (int): Number of records to skip. Defaults to 0.
        limit (int): Maximum number of records to return. Defaults to 10.
        db (Session): Database session dependency.

    Returns:
        List[QRCodeSchema]: List of QR codes.
    """
    qr_codes = db.query(QRCode).offset(skip).limit(limit).all()
    return qr_codes
