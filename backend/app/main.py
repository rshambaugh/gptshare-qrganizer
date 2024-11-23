from fastapi import FastAPI
from routers import qr_codes
from app.core.exceptions import custom_http_exception_handler, CustomHTTPException
from app.routers import qr_codes
from app.routers import items

app = FastAPI()
app.title = 'QRganizer API'
app.description = 'An API for managing QR codes with endpoints for creation and retrieval.'
app.version = '1.0.0'
app.add_exception_handler(CustomHTTPException, custom_http_exception_handler)
app.include_router(qr_codes.router)

# Include routers
app.include_router(items.router)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from the frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
