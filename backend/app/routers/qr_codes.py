from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# Sample data representing QR codes
qr_codes = [
    {"id": 1, "name": "QR Code 1", "url": "http://example.com/1"},
    {"id": 2, "name": "QR Code 2", "url": "http://example.com/2"},
    # Add more QR codes as needed
]

@router.get("/qr_codes/", response_model=List[dict])
async def read_qr_codes():
    """
    Retrieve a list of QR codes.
    """
    if not qr_codes:
        raise HTTPException(status_code=404, detail="No QR codes found")
    return qr_codes
