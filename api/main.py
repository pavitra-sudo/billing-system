# main.py

from datetime import datetime

from fastapi import FastAPI
from api.routers.tenant import tenantCreate, tenantLogin
from api.routers.shop.product import createProduct, deleteProduct
from api.database.db import PublicBase, engine
from api.middleware.schemaFetch import SchemaMiddleware
from time import sleep

app = FastAPI(title="Billing System API")


while True:
    try:
        PublicBase.metadata.create_all(bind=engine)
        
        break
    except Exception as e:
        print(f"Error connecting to database: {e} at {datetime.now()}" )
        sleep(5) # wait before retrying
        
        
        
app.add_middleware(SchemaMiddleware)  # global middleware for schema fetching
  

# tenant  routers
app.include_router(tenantCreate.router)
app.include_router(tenantLogin.router)

# shop routers
app.include_router(createProduct.router)
app.include_router(deleteProduct.router)



@app.get("/")
def root():
    return {"message": "API is running"}