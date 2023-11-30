
from fastapi import APIRouter

router = APIRouter( 
    prefix='/userapi' 
) 

@router.get('/api1') 
async def api1(): 
    pass 