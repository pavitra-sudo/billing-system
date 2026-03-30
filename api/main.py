# main.py
from fastapi import FastAPI
from datetime import datetime
from api.models.tenant.tenant import Tenant
from api.routers.shop import products
from api.routers.tenant import  tenant
from api.database.db import PublicBase, engine
from api.middleware.auth2Middleware import AuthMiddleware
from time import sleep


app = FastAPI(title="Billing System API")


while True:
    try:
        PublicBase.metadata.create_all(bind=engine)
        
        break
    except Exception as e:
        print(f"Error connecting to database: {e} at {datetime.now()}" )
        sleep(5) # wait before retrying
        
        
        

#app.add_middleware(AuthMiddleware)  # global middleware for auth


# tenant  routers
app.include_router(tenant.router)

# product routers
app.include_router(products.router)





@app.get("/")
def root():
    return {"message": "API is running"}