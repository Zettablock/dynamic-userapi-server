
from fastapi import APIRouter

router = APIRouter( 
    prefix='/userapi' 
) 

@router.get('/api2') 
async def api2(): 
    pass 