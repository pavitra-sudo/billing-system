# main.py

from datetime import datetime

from fastapi import FastAPI
from api.routers.tenant import createTenant, loginTenant
from api.routers.shop.product import createProduct, deleteProduct, getProduct, updateProduct
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
        
        
        

app.add_middleware(AuthMiddleware)  # global middleware for auth
  

# tenant  routers
app.include_router(createTenant.router)
app.include_router(loginTenant.router)

# product routers
app.include_router(createProduct.router)
app.include_router(deleteProduct.router)
app.include_router(updateProduct.router)
app.include_router(getProduct.router)




@app.get("/")
def root():
    return {"message": "API is running"}