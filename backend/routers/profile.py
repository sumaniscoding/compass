from fastapi import APIRouter

router = APIRouter(
    prefix='/profile',
    tags=['profile'],
    responses={404: {'description': 'not found'}}
)

@router.get('/')
async def profile():
    return "profile"