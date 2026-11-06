from fastapi import APIRouter, Depends, HTTPException, Response

from open_webui.utils.auth import get_verified_user

router = APIRouter()

DSH_USERS = {
    'changjun.z@gmail.com': 'cj',
    'darcyzhangdx@gmail.com': 'dx',
}


@router.get('/check')
async def check(user: str, current=Depends(get_verified_user)):
    if DSH_USERS.get((current.email or '').lower()) != user:
        raise HTTPException(status_code=403)
    return Response(status_code=204)
