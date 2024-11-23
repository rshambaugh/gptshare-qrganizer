from fastapi import APIRouter

router = APIRouter()

@router.get("/items", tags=["Items"])
async def read_items():
    return {"message": "List of items"}

@router.post("/items", tags=["Items"])
async def create_item(item: dict):
    return {"message": f"Item created: {item}"}
