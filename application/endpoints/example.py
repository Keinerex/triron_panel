from fastapi import APIRouter

api_router = APIRouter(
    prefix="/example",
    tags=["example"],
)


@api_router.get("/", )
def example():
    return {"Example": "example"}
