from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from pydantic import BaseModel

# Usa la MISMA clave y algoritmo que en tu API de autenticación
SECRET_KEY = "clave_secreta_64_caracteres_1234567890abcdef1234567890abcdef1234567890abcd"
ALGORITHM = "HS256"

# Esta URL no se usará aquí, pero FastAPI la requiere igual
bearer_scheme = HTTPBearer()

class TokenData(BaseModel):
    id: int
    name: str
    role: str

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> TokenData:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        name = payload.get("name")
        role = payload.get("role")

        if user_id is None or name is None or role is None:
            raise credentials_exception

        return TokenData(id=int(user_id), name=name, role=role)

    except JWTError:
        raise credentials_exception
