from fastapi import FastAPI
from routers.foods import food_router 
from routers.restaurant import res_router
from db.database import Base, engine

### router -> importing foods router
from routers.foods import food_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

##step -2 
app.include_router(food_router)

## decorator function
@app.get("/welcome")
def greeting():
    return{"message": "Welcome to my server"}

app.include_router(food_router)
app.include_router(res_router)















    

