from app.schemas.schemas import QRCode, QRCodeCreate

def test_qr_code_schema():
    sample_data = {"id": 1, "data": "Sample QR Code", "created_at": "2024-01-01T00:00:00"}
    qr_code = QRCode(**sample_data)
    assert qr_code.id == 1
    assert qr_code.data == "Sample QR Code"
    assert qr_code.created_at == "2024-01-01T00:00:00"

def test_qr_code_create_schema():
    sample_data = {"data": "Sample QR Code"}
    qr_code_create = QRCodeCreate(**sample_data)
    assert qr_code_create.data == "Sample QR Code"
