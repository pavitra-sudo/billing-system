# main.py

from fastapi import FastAPI
from api.routers.tenant import tenantCreate
from api.database.db import PublicBase, engine

app = FastAPI(title="Billing System API")


PublicBase.metadata.create_all(bind=engine)  

# include routers
app.include_router(tenantCreate.router)


@app.get("/")
def root():
    return {"message": "API is running"}