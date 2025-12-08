from fastapi import APIRouter,Depends
from schemas.foods import Foods_schemas
from dependencies import connect_db
from sqlalchemy.orm import Session

##
from models.foods import Foods



food_router=APIRouter(
    prefix="/foods",
    tags=["FOODS"]
    )

## get method
@food_router.get("/")
def get_all_foods():
    return{"message":""}

## get method
@food_router.get("/{id}")
def  get_all_foods(id:int):
    return {"message":""}

# POST
@food_router.post("/")
def get_all_foods(new_food:Foods_schemas, dbs: Session = Depends(connect_db)):
    some_food_name = new_food.food_name
    some_price = new_food.price
    some_qty = new_food.qty
    something_avl = new_food.availability
    # food new model
    new_entry = Foods(
        food_name=some_food_name,
        price=some_price,
        qty=some_qty,
        availability=something_avl,
    )
    # adding the row
    dbs.add(new_entry)

    # committing the row
    dbs.commit()

    # refresh the table
    dbs.refresh(new_entry)
    return new_entry

@food_router.put("/{id}")
def get_all_foods(latest_food:Foods_schemas):
    return {"message":""}

@food_router.delete("/{id}")
def delete_foods(latest_food:Foods_schemas):
    return {"message":""}











