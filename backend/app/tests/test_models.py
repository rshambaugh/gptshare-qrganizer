from app.models.models import QRCode
from app.core.database import Base

def test_qr_code_model():
    assert QRCode.__tablename__ == "qr_codes"
    assert "id" in QRCode.__table__.columns.keys()
    assert "data" in QRCode.__table__.columns.keys()
    assert "created_at" in QRCode.__table__.columns.keys()
