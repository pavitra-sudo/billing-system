# middleware/auth_middleware.py
import os
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import JSONResponse
from jose import jwt, JWTError
from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY","None") # In production, use a secure method to store this
ALGORITHM = os.getenv("ALGORITHM", "HS256")


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # ✅ Allow preflight requests
        if request.method == "OPTIONS":
            return await call_next(request)

        path = request.url.path
        print(" PATH:", path)

        public_prefixes = (
            "/api/auth/register",
            "/api/auth/login",
            "/docs",
            "/openapi",
            "/redoc"
        )

        if path.startswith(public_prefixes):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        print("🔐 HEADER:", auth_header)

        if not auth_header:
            return JSONResponse(status_code=401, content={"detail": "Authorization header missing"})

        token = auth_header.replace("Bearer ", "")

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            schema = payload.get("schema")
            tenant_id = payload.get("tenant_id")

            if not schema or not schema.startswith("schema_shop_"):
                return JSONResponse(status_code=401, content={"detail": "Invalid schema"})

            request.state.schema = schema
            request.state.tenant_id = tenant_id

        except JWTError:
            return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

        return await call_next(request)