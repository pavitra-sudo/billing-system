# main.py

from fastapi import FastAPI
from api.routers import shop_owner
from api.database.db import PublicBase, engine

app = FastAPI(title="Billing System API")


PublicBase.metadata.create_all(bind=engine)  # create public tables (shop_owner, etc.)

# include routers
app.include_router(shop_owner.router)


@app.get("/")
def root():
    return {"message": "API is running"}