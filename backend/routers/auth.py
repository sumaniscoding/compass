from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={404: {'description': 'not found'}}
)

@router.get('/')
async def login():
    return "login"