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
    db_qr_code = QRCode(data=qr_code.data)
    db.add(db_qr_code)
    db.commit()
    db.refresh(db_qr_code)
    return db_qr_code

@router.get("/qr_codes/{qr_code_id}", response_model=QRCodeSchema)
def read_qr_code(qr_code_id: int, db: Session = Depends(get_db)):
    db_qr_code = db.query(QRCode).filter(QRCode.id == qr_code_id).first()
    if db_qr_code is None:
        raise HTTPException(status_code=404, detail="QR code not found")
    return db_qr_code
