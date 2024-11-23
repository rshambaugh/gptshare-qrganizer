from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.models import QRCode
from app.schemas.schemas import QRCode as QRCodeSchema
from app.core.database import get_db

router = APIRouter()

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

@router.get("/qr_codes/{qr_code_id}", response_model=QRCodeSchema)
async def read_qr_code(qr_code_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a QR code by ID.

    Args:
        qr_code_id (int): The ID of the QR code to retrieve.
        db (Session): Database session dependency.

    Returns:
        QRCodeSchema: The requested QR code.

    Raises:
        HTTPException: If the QR code is not found.
    """
    qr_code = db.query(QRCode).filter(QRCode.id == qr_code_id).first()
    if not qr_code:
        raise HTTPException(status_code=404, detail="QR code not found")
    return qr_code
