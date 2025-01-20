from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=dict[str, str])
async def read_root() -> dict[str, str]:
    return {"message": "Hello World"}
