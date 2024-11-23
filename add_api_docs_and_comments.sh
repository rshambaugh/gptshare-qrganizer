#!/bin/bash

# Define paths
BACKEND_PATH="$HOME/projects/qrganizer/backend/app"
MAIN_PY="$BACKEND_PATH/main.py"
QR_CODES_ROUTER="$BACKEND_PATH/routers/qr_codes.py"

# Step 1: Enhance API Documentation in `main.py`
echo "Enhancing API documentation in main.py..."
if [ -f "$MAIN_PY" ]; then
  sed -i "/app = FastAPI()/a app.title = 'QRganizer API'\napp.description = 'An API for managing QR codes with endpoints for creation and retrieval.'\napp.version = '1.0.0'" "$MAIN_PY"
else
  echo "Error: main.py not found. Skipping API documentation enhancements."
fi

# Step 2: Add comments and docstrings to `qr_codes.py`
echo "Adding comments and docstrings to qr_codes.py..."
if [ -f "$QR_CODES_ROUTER" ]; then
  sed -i "1s|^|\"\"\"\nRoutes for QR code operations.\n\n- POST /qr_codes/ : Create a new QR code.\n- GET /qr_codes/{qr_code_id} : Retrieve a QR code by ID.\n\"\"\"\n\n|" "$QR_CODES_ROUTER"

  sed -i "/def create_qr_code/a \\    \"\"\"\n    Create a new QR code.\n\n    Args:\n        qr_code (QRCodeCreate): The data for the new QR code.\n        db (Session): The database session.\n\n    Returns:\n        QRCode: The created QR code object.\n    \"\"\"" "$QR_CODES_ROUTER"

  sed -i "/def read_qr_code/a \\    \"\"\"\n    Retrieve a QR code by ID.\n\n    Args:\n        qr_code_id (int): The ID of the QR code to retrieve.\n        db (Session): The database session.\n\n    Returns:\n        QRCode: The requested QR code object, if found.\n\n    Raises:\n        HTTPException: If the QR code is not found.\n    \"\"\"" "$QR_CODES_ROUTER"
else
  echo "Error: qr_codes.py not found. Skipping docstring additions."
fi

echo "API documentation and code comments have been added!"
