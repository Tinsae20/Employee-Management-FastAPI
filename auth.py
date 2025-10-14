from fastapi import Request, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from typing import cast
from database import SUPABASE_JWT_SECRET

security = HTTPBearer()

async def auth_middleware(request: Request, call_next):
    token = request.cookies.get('access_token')
    if token and token.startswith('Bearer '):
        token = token.split(' ')[1]
        request.headers.__dict__['_list'].append(
            (b"authorization", f"Bearer {token}".encode())
        )

    resonse = await call_next(request)
    return resonse

def get_current_user(crendentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = crendentials.credentials
        if token.startswith('Bearer '):
            token = token.split(' ')[1]
        
        payload = jwt.decode(token, cast(str,SUPABASE_JWT_SECRET), algorithms=['HS256'],options={'verify_aud': False})
        user_id = payload.get('sub')
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials.')
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has expired.')
    except jwt.PyJWKError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')