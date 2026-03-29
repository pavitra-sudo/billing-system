# main.py

from datetime import datetime

from fastapi import FastAPI
from api.routers.tenant import tenantCreate
from api.database.db import PublicBase, engine
from time import sleep

app = FastAPI(title="Billing System API")


while True:
    try:
        PublicBase.metadata.create_all(bind=engine)
        
        break
    except Exception as e:
        print(f"Error connecting to database: {e} at {datetime.now()}" )
        sleep(5) # wait before retrying
        
        
        
  
  

# include routers
app.include_router(tenantCreate.router)


@app.get("/")
def root():
    return {"message": "API is running"}