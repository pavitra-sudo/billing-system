# routes/tenant_auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from api.database.db import get_db
from api.models.tenant.tenantModel import Tenant
from api.auth.hashing import  verify_password
from api.auth.token import create_access_token



router = APIRouter(prefix="/login-tenant",
    tags=["Tenant Management"])


@router.post("/", status_code=status.HTTP_200_OK)
def tenant_login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(Tenant).filter(Tenant.email == request.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email")

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    # 🔥 include schema in token
    token = create_access_token({
        "sub": user.email,
        "schema": user.schema_name
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "schema": user.schema_name  # optional (debugging)
    }
    
