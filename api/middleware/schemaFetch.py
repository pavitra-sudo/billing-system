# middleware/schema_middleware.py

from starlette.middleware.base import BaseHTTPMiddleware
from api.auth.token import decode_token
from sqlalchemy import text


class SchemaMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        token = request.headers.get("Authorization")

        if token:
            token = token.replace("Bearer ", "")
            payload = decode_token(token)

            if payload:
                schema = payload.get("schema")

                if schema:
                    request.state.schema = schema

        response = await call_next(request)
        return response