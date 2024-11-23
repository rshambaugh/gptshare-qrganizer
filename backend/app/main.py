from fastapi import FastAPI
from app.routers import items

app = FastAPI()

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
