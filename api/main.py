# main.py

from fastapi import FastAPI
from api.routers.tenant import create_tenant
from api.database.db import PublicBase, engine

app = FastAPI(title="Billing System API")


PublicBase.metadata.create_all(bind=engine)  # create public tables (shop_owner, etc.)

# include routers
app.include_router(create_tenant.router)


@app.get("/")
def root():
    return {"message": "API is running"}