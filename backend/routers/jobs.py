from fastapi import APIRouter

router = APIRouter(
    prefix='/jobs',
    tags=['jobs'],
    responses={404: {'description': 'not found'}}
)

@router.get('/')
async def dashboard():
    return "dashboard"